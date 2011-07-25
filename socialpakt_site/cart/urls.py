### -*- coding: utf-8 -*- ####################################################

from django.conf.urls.defaults import *
from django.utils.translation import ugettext_lazy as _


urlpatterns = patterns('cart.views',

    url('^$', 'show_cart', {
        'template_name': 'cart/listing.html',
    }, name="show_cart"),
    
    url('^add/(?P<content_type_pk>[\d]+)/(?P<object_pk>[\d]+)/(?P<quantity>[\d]+)/$', 
        'add_to_cart', {}, name="add_to_cart"),
    
    url('^restore/(?P<item_pk>[\d]+)/$', 'restore_item', {
        'success_message': _('Restored successfully.'),
    }, name="restore_item"),
    
    url('^disable/(?P<item_pk>[\d]+)/$', 'disable_item', {
        'success_message': _('Disabled successfully.'),
    }, name="disable_item"),
    
    url('^change_quantity/(?P<pk_param>[\w]+)/(?P<param_name>[\w]+)/$', 'change_quantity', {}, name='change_quantity'), 
    
    url('^remove/(?P<item_pk>[\d]+)/$', 'remove_item', {
        'success_message': _('Deleted successfully.'),
    }, name="remove_item"),
    
    url(r'^clear/$', 'clear', name='clear_cart'),
    
    url(r'^get_amount/$', 'get_amount', name='get_amount'),
    url(r'^get_count/$', 'get_count', name='get_count'),

)
