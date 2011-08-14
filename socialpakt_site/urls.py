from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from catalog.views import *
from partners.models import *
from django.views.generic import DetailView, TemplateView, CreateView

from splash.models import SignupForm

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'socialpakt_site.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    url(r'^$', CreateView.as_view(form_class=SignupForm, template_name="splash/splash.html", success_url="/thankyou/"), name='spashpage', ),
    url(r'^welcome_video/$', CreateView.as_view(form_class=SignupForm, template_name="splash/splash.html", success_url="/thankyou/"), name='spashpage_video', ),
    url(r'^thankyou/$', TemplateView.as_view(template_name="splash/splash.html"), name='thankyou', ),
        
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^app/$', CatalogHomeView.as_view(), name='home', ),
    #url(r'^shirt/(?P<slug>\w+)/$', CatalogHomeView.as_view(), name='shirt', ),
    #url(r'^artist/(?P<slug>\w+)/$', 
    #	DetailView.as_view(queryset=Partner.objects.filter(partner_type="ART"),context_object_name="partner"), name='artist', ),
    #url(r'^nonprofit/(?P<slug>\w+)/$', 
    #	DetailView.as_view(queryset=Partner.objects.filter(partner_type="NPO"),context_object_name="partner"), name='nonprofit', ),

    #url(r'^cart/', include('cart.urls')),
)
