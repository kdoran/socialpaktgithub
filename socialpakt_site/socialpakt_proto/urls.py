from django.conf.urls.defaults import *
from django.views.generic import DetailView, TemplateView, CreateView, ListView

urlpatterns = patterns('socialpakt_proto.views',

    url(r'^home/$', TemplateView.as_view(template_name="index.html"), name='index', ),

)
