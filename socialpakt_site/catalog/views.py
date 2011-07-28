from django.views.generic import TemplateView
from models import *
from django.conf import settings

class CatalogHomeView(TemplateView):
    template_name = "catalog/product.html"

    def get_context_data(self, **kwargs):
        products = Product.objects.filter(active=True).order_by('-date_expires')

        # todo if we have a slug, get that instead
        product = products[:1]

        return {
            'product' : product[0] if len(products) else None,
            'settings' : settings,
            'params': kwargs,
        }