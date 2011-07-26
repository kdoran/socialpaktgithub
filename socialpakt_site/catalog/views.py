from django.views.generic import TemplateView
from models import *
from django.conf import settings

class CatalogHomeView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):

        return {
            'settings' : settings,
            'params': kwargs,
        }