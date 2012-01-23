from django.conf import settings as django_settings
from models import *

def categories(request):
	return {
		'product_categories':ProductCategory.objects.all().order_by('display_order'),
		}