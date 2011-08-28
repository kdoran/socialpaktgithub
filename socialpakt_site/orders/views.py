# Create your views here.
import urllib
from django.http import *
 
from globals.foxycart import FoxyData
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from django.template.loader import get_template
from django.template import Context, Template


from models import Order
from catalog.models import *

transaction_fields = [
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

@csrf_exempt 
def foxyfeed(request):
    if request.POST and 'FoxyData' in request.POST:
        try:
            data = FoxyData.from_crypted_str(urllib.unquote_plus(request.POST['FoxyData']), settings.FOXYCART_DATAFEED_KEY)	# IMPORTANT: unquote_plus is necessary for the non-ASCII binary that FoxyCart sends.
            for transaction in data.transactions:
                order = Order(order_xml=data.markup)
                order.order_id = transaction.id
                for f in transaction_fields:
                    setattr(order, f, getattr(transaction, f))

                items = ""
                for item in transaction.items:
                    product_code = item["product_code"]
                    product_variation = item["detail"]["shirt"]
                    quantity = item["product_quantity"]

                    product = Product.objects.get(slug=product_code)
                    variation = product.productvariation_set.get(description=product_variation)

                    product.total_sold += int(quantity)
                    product.save()

                    variation.num_ordered += int(quantity)
                    variation.save()

                    items += "Product Name:" + item["product_name"] + "\n"
                    items += "Product Code:" + product_code + "\n"
                    items += "Product Quantity:" + quantity + "\n"
                    items += "Product Variation:" + product_variation + "\n"
                    items += "\n"

                order.items_ordered = items
                order.save()

            return HttpResponse('foxy')

        except Exception, e:
            # Something went wrong, handle the error...
            raise

    return HttpResponseForbidden('Unauthorized request.')  # No FoxyData?  Not a POST?  We don't speak that.