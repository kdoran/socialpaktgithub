# Create your views here.
import urllib
from django.http import *
 
from globals.foxycart import FoxyData		# I put foxycart.py in a 'utils' module
from django.conf import settings

from models import Order
 
def foxyfeed(request):
    if request.POST and 'FoxyData' in request.POST:
        try:
      		data = FoxyData.from_crypted_str(urllib.unquote_plus(request.POST['FoxyData']), settings.FOXYCART_DATAFEED_KEY)	# IMPORTANT: unquote_plus is necessary for the non-ASCII binary that FoxyCart sends.
      		for transaction in data.transactions:
        		order = Order(order_xml=str(data))
        		order.save()
 
      		return HttpResponse('foxy')
 
    	except Exception, e:
	  		# Something went wrong, handle the error...
      		raise
 
  	return HttpResponseForbidden('Unauthorized request.')  # No FoxyData?  Not a POST?  We don't speak that.