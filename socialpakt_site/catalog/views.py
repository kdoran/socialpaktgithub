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

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form,**kwargs))

    def get_context_data(self, **kwargs):
        if "slug" in kwargs:
            product = get_object_or_404(Product, slug=kwargs["slug"])
            cat = product.category
        else:
            # check for a category first
            cat = None
            if 'category' in kwargs:
                cat = ProductCategory.objects.filter(slug=kwargs['category'])[0]
            else:
                cat = ProductCategory.objects.all().order_by('?')[0]
            products = Product.objects.filter(active=True, category=cat, featured=True)
            if not products:
                # go find a product to display
                products = Product.objects.filter(active=True, category=cat).order_by('-date_expires')
            product = products[:1]
            product = product[0] if len(products) else None # need to refactor this

        context = {
            'category' : cat,
            'product' : product,
            'previous_products' : Product.objects.filter(active=True).order_by('date_expires'),
            'variations' : product.productvariation_set.all().order_by('display_order') if product else None,
            'can_add_to_cart' : product.for_sale if product else False,
            'product_variation_contenttype' : ContentType.objects.get(model="productvariation"),
            'now' : datetime.now(),
        }

        kwargs.update(context)

        # call get context data for ModelFormMixin
        model_form_context = ModelFormMixin.get_context_data(self, **kwargs)
        kwargs.update(model_form_context)
        return kwargs