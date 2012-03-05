# Create your views here.
import urllib
from django.http import *
 
from globals.foxycart import FoxyData
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from django.template.loader import get_template
from django.template import Context, Template

from django.contrib.auth.decorators import login_required

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

                    quantity_int = int(quantity)

                    product.total_sold += quantity_int
                    product.save()

                    variation.num_ordered += quantity_int

                    if product.has_inventory:
                        variation.inventory = variation.inventory-quantity_int

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

@login_required(login_url='/')
def orderemails(request, product_code):
    if request.user.is_staff:
        emails = ""
        orders = Order.objects.filter(items_ordered__contains=product_code)
        for o in orders:
            emails += o.customer_email + "<br/>"
        return HttpResponse(emails)
    else:
        return HttpReponse("")


@login_required(login_url='/')
def orderlist(request, product_code):
    if request.user.is_staff:
        items = "PONumber,OrderDate,ConsigneeFullName,ConsigneeAddress1,ConsigneeAddress2,ConsigneeCity,ConsigneeState,ConsigneeZip,ConsigneeCountry,ConsigneePhone,ConsigneeEmail,ItemSKU,ItemQuantity,Carrier,ShippingLevel,Comments,ConfirmationNumber</br>"
        orders = Order.objects.filter(items_ordered__contains=product_code)
        for o in orders:
            try:
                data = FoxyData.from_str(urllib.unquote_plus(o.order_xml))
                for transaction in data.transactions:
                    for item in transaction.items:
                        product_code = item["product_code"]
                        product_variation = item["detail"]["shirt"]
                        quantity = item["product_quantity"]
                    
                        order = o.order_id+","+str(o.transaction_date)+","

                        if o.shipping_first_name and o.shipping_first_name != "" and o.shipping_last_name and o.shipping_last_name != "":
                            consignee_fullname = o.shipping_first_name +" "+ o.shipping_last_name
                        else:
                            consignee_fullname = o.customer_first_name +" "+ o.customer_last_name

                        order += '"'+consignee_fullname + '",'

                        if o.shipping_address1 and o.shipping_address1 != "":
                            consignee_address1 = o.shipping_address1
                        else:
                            consignee_address1 = o.customer_address1

                        order += '"'+consignee_address1 + '",'

                        if o.shipping_address2 and o.shipping_address2 != "":
                            consignee_address2 = o.shipping_address2
                        else:
                            consignee_address2 = o.customer_address2

                        order += '"'+consignee_address2 + '",'
                        
                        if o.shipping_city and o.shipping_city != "":
                            consignee_city = o.shipping_city
                        else:
                            consignee_city = o.customer_city

                        order += '"'+consignee_city + '",'    

                        if o.shipping_state and o.shipping_state != "":
                            consignee_state = o.shipping_state
                        else:
                            consignee_state = o.customer_state

                        order += '"'+consignee_state + '",'
                        
                        if o.shipping_postal_code and o.shipping_postal_code != "":
                            consignee_postal_code = o.shipping_postal_code
                        else:
                            consignee_postal_code = o.customer_postal_code

                        order += '"'+consignee_postal_code + '",'

                        if o.shipping_country and o.shipping_country != "":
                            consignee_country = o.shipping_country
                        else:
                            consignee_country = o.customer_country

                        order += '"' + consignee_country + '",'

                        if o.shipping_phone and o.shipping_phone != "":
                            consignee_phone = o.shipping_phone
                        else:
                            consignee_phone = o.customer_phone

                        order += '"'+consignee_phone + '",'+o.customer_email+","+product_code+"-"+product_variation+","+quantity+",USPS"+",,,<br/>"
                        items += order

            except Exception, e:
                # Something went wrong, handle the error...
                raise

        return HttpResponse(items)

    else:
        return HttpReponse("")
