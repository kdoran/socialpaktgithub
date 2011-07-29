from django.views.generic import TemplateView
from models import *
from django.conf import settings

from django.shortcuts import get_object_or_404

class CatalogHomeView(TemplateView):
    template_name = "catalog/product.html"

    def get_context_data(self, **kwargs):
        products = Product.objects.filter(active=True).order_by('-date_expires')

        if "slug" in kwargs:
            product = get_object_or_404(Product, slug=kwargs["slug"])
        else:
            product = products[:1]
            product = product[0] if len(products) else None # need to refactor this

        return {
            'request' : self.request,
            'product' : product,
            'settings' : settings,
            'params': kwargs,
        }