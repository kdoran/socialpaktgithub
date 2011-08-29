"""
Utilities for decrypting and parsing a FoxyCart datafeed.
"""
from xml.dom.minidom import parseString
from datetime import datetime
 
# Thanks, Wikipedia: http://en.wikipedia.org/wiki/RC4#Implementation
class ARC4:
    def __init__(self, key = None):
        self.state = range(256) # Initialize state array with values 0 .. 255
        self.x = self.y = 0 # Our indexes. x, y instead of i, j
 
        if key is not None:
            self.init(key)
 
    # KSA
    def init(self, key):
        for i in range(256):
            self.x = (ord(key[i % len(key)]) + self.state[i] + self.x) & 0xFF
            self.state[i], self.state[self.x] = self.state[self.x], self.state[i]
        self.x = 0
 
    # PRGA
    def crypt(self, input):
        output = [None]*len(input)
        for i in xrange(len(input)):
            self.x = (self.x + 1) & 0xFF
            self.y = (self.state[self.x] + self.y) & 0xFF
            self.state[self.x], self.state[self.y] = self.state[self.y], self.state[self.x]
            r = self.state[(self.state[self.x] + self.state[self.y]) & 0xFF]
            output[i] = chr(ord(input[i]) ^ r)
        return ''.join(output)
 
 
class FoxyData:
  DateFmt = '%Y-%m-%d'
  DateTimeFmt = '%Y-%m-%d %H:%M:%S'

  fields = [
      'id',
      'store_id',
      'store_version',
      'is_test',
      'transaction_date',
      'processor_response',
      'customer_id',
      'is_anonymous',
      'customer_first_name',
      'customer_last_name',
      'customer_company',
      'customer_address1',
      'customer_address2',
      'customer_city',
      'customer_state',
      'customer_postal_code',
      'customer_country',
      'customer_phone',
      'customer_email',
      'customer_ip',
      'shipping_first_name',
      'shipping_last_name',
      'shipping_company',
      'shipping_address1',
      'shipping_address2',
      'shipping_city',
      'shipping_state',
      'shipping_postal_code',
      'shipping_country',
      'shipping_phone',
      'shipto_shipping_service_description',
      'purchase_order',
      'cc_number_masked',
      'cc_type',
      'cc_exp_month',
      'cc_exp_year',
      'product_total',
      'tax_total',
      'shipping_total',
      'order_total',
      'payment_gateway_type',
      'receipt_url',
      'taxes',
      'discounts',
      'customer_password',
      'customer_password_salt',
      'customer_password_hash_type',
      'customer_password_hash_config',
  ]

  item_fields = [
      'product_code',
      'product_name',
      'product_quantity',
  ]
 
  class Transaction:
    def __init__(self, node):
      def extract_kv_node(node, key_name):
        el = node.getElementsByTagName(key_name)
        return len(el) > 0 and el[0].firstChild and hasattr(el[0].firstChild, "data") and el[0].firstChild.data or ''
 
      for k in FoxyData.fields:
          setattr(self,k,extract_kv_node(node, k))

      if hasattr(self, "id"):
        self.order_id = self.id

      self.transaction_date = datetime.strptime(
       extract_kv_node(node, 'transaction_date'), FoxyData.DateTimeFmt)
 
      self.attributes = attrs = {}
      self.items = items = attrs['items'] = []
 
      self.custom_fields = attrs['custom_fields'] = {}
      for custom_field in node.getElementsByTagName('custom_field'):
        self.custom_fields[extract_kv_node(custom_field, 'custom_field_name')] = \
         extract_kv_node(custom_field, 'custom_field_value')
 
      self.transaction_details = attrs['detail'] = []
      for details in node.getElementsByTagName('transaction_detail'):
        item = {}
        for k in FoxyData.item_fields:
          item[k] = extract_kv_node(details, k)

        detail = item['detail'] = {}
        for detail_opt in details.getElementsByTagName('transaction_detail_option'):
          detail[extract_kv_node(detail_opt, 'product_option_name')] = \
           extract_kv_node(detail_opt, 'product_option_value')
 
        items.append(item)
 
  def __init__(self, markup):
    self.markup = markup
    self.doc = parseString(self.markup)
    self.transactions = []
 
    for transaction in self.doc.getElementsByTagName('transaction'):
      self.transactions.append(FoxyData.Transaction(transaction))
 
  def __str__(self):
    return str(self.markup)
 
 
  @classmethod
  def from_str(self, data_str):
    return FoxyData(data_str)
 
  """
  Given a string containing RC4-crypted FoxyCart datafeed XML and the
  cryptographic key, decrypt the contents and create a FoxyData object
  containing all of the Transactions in the data feed.
  """
  @classmethod
  def from_crypted_str(self, data_str, crypt_key):
    data = ARC4(crypt_key).crypt(data_str)
    return FoxyData.from_str(data)
 
  def __len__(self):
    return len(self.transactions)