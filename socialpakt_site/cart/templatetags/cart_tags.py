### -*- coding: utf-8 -*- ####################################################

from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from native_tags.decorators import function

from cart.cart import Cart

@function
def add_to_cart_url(obj, quantity):
    ct_pk = ContentType.objects.get_for_model(obj).pk
    
    return reverse('add_to_cart', current_app='cart', kwargs={
        'content_type_pk': ct_pk, 
        'object_pk': obj.pk, 
        'quantity': quantity
    })


def get_cart_count(request):
    return Cart(request).get_count()

get_cart_count = function(get_cart_count, takes_request=1)


def get_cart_amount(request):
    return Cart(request).cart.get_amount()

get_cart_amount = function(get_cart_amount, takes_request=1)
