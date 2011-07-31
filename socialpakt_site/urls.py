from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from catalog.views import *
from partners.models import *
from django.views.generic import DetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'socialpakt_site.views.home', name='home'),
    # url(r'^socialpakt_site/', include('socialpakt_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', CatalogHomeView.as_view(), name='home', ),
    url(r'^shirt/(?P<slug>\w+)/$', CatalogHomeView.as_view(), name='shirt', ),
    url(r'^artist/(?P<slug>\w+)/$', 
    	DetailView.as_view(queryset=Partner.objects.filter(partner_type="ART"),context_object_name="partner"), name='artist', ),
    url(r'^nonprofit/(?P<slug>\w+)/$', 
    	DetailView.as_view(queryset=Partner.objects.filter(partner_type="NPO"),context_object_name="partner"), name='nonprofit', ),
)
