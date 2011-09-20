from django.views.generic import TemplateView
from django.views.generic.edit import ModelFormMixin, ProcessFormView
from models import *
from django.conf import settings
from datetime import datetime

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from splash.models import *

class CatalogHomeView(ModelFormMixin, ProcessFormView, TemplateView):
    template_name = "catalog/product.html"
    form_class = SignupForm
    success_url = "."
    object = None

    def get_context_data(self, **kwargs):
        products = Product.objects.filter(active=True).order_by('-date_expires')

        if "slug" in kwargs:
            product = get_object_or_404(Product, slug=kwargs["slug"])
        else:
            product = products[:1]
            product = product[0] if len(products) else None # need to refactor this

        context = {
            'product' : product,
            'can_add_to_cart' : product.date_expires >= datetime.now(),
            'product_variation_contenttype' : ContentType.objects.get(model="productvariation"),
        }

        kwargs.update(context)

        # call get context data for ModelFormMixin
        model_form_context = ModelFormMixin.get_context_data(self, **kwargs)

        kwargs.update(model_form_context)

        print kwargs

        return kwargs