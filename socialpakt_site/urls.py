from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from catalog.views import *
from catalog.models import *
from partners.models import *
from orders.views import *
from django.views.generic import DetailView, TemplateView, CreateView, ListView

from splash.models import SignupForm

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'socialpakt_site.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    # url(r'^$', CreateView.as_view(form_class=SignupForm, template_name="splash/splash.html", success_url="/thankyou/"), name='spashpage', ),
    url(r'^welcome_video/$', CreateView.as_view(form_class=SignupForm, template_name="splash/splash.html", success_url="/thankyou/"), name='spashpage_video', ),
    url(r'^thankyou/$', TemplateView.as_view(template_name="splash/splash.html"), name='thankyou', ),

    url(r'^cart/checkout/$', TemplateView.as_view(template_name="foxycart/checkout.html"), name='fc_checkout', ),
    url(r'^cart/details/$', TemplateView.as_view(template_name="foxycart/cart.html"), name='fc_cart', ),
    url(r'^cart/receipt/$', TemplateView.as_view(template_name="foxycart/receipt.html"), name='fc_cart', ),

    url(r'^order/$', foxyfeed, name="order"),
    url(r'^order/emails/(?P<product_code>\w+)/$', orderemails),
    url(r'^order/list/(?P<product_code>\w+)/$', orderlist),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', CatalogHomeView.as_view(), name='home', ),
    url(r'^shirt/(?P<slug>\w+)/$', CatalogHomeView.as_view(), name='shirt', ),
    url(r'^artist/(?P<slug>\w+)/$', 
    	DetailView.as_view(queryset=Partner.objects.filter(partner_type="ART"),context_object_name="partner"), name='artist', ),
    url(r'^nonprofit/(?P<slug>\w+)/$', 
    	DetailView.as_view(queryset=Partner.objects.filter(partner_type="NPO"),context_object_name="partner"), name='nonprofit', ),

    url(r'^artists/$', ListView.as_view(queryset=Partner.objects.filter(partner_type="ART"), template_name_suffix="_artistlist"), name='artists'),
    url(r'^nonprofits/$', ListView.as_view(queryset=Partner.objects.filter(partner_type="NPO"), template_name_suffix="_npolist"), name='npos'),
    url(r'^shirts/$', ListView.as_view(queryset=Product.objects.filter(active=True)), name='shirts'),

    url(r'^cart/', include('cart.urls')),
    url(r'^proto/', include('socialpakt_proto.urls')),
)
