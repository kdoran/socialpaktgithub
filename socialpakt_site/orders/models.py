from django.db import models

# Create your models here.
class Order(object):
	"""An order received from FoxyCart"""

	order_xml = models.TextField()
	fulfilled = models.BooleanField(default=False)

	def __str__(self):
		return self.order_xml
		