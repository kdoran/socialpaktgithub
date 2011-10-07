from django.db import models

from partners.models import Partner

# Create your models here.
class Product(models.Model):
	"""Model representing a tshirt for SocialPakt"""

	slug = models.SlugField(max_length=255, db_index=True)
	title = models.CharField(max_length=255)
	cart_title = models.CharField(max_length=255, default="This week's shirt")
	description = models.TextField()
	call_to_action = models.CharField(max_length=255, default="")

	active = models.BooleanField(default=False, db_index=True)
	date_expires = models.DateTimeField(db_index=True)

	artist = models.ForeignKey(Partner, related_name="artist_on_set")
	benefits = models.ForeignKey(Partner, related_name="benefits_from_set")

	price = models.FloatField()
	donation_amount = models.FloatField(default=6.0)
	goal = models.FloatField(default=1200.0)
	total_sold = models.IntegerField(default=0)

	def total_raised(self):
		return self.total_sold*self.donation_amount

	def distance_to_goal(self):
		return self.total_raised() / self.goal * 100.0

	def __str__(self):
		return self.slug
		
class ProductVariation(models.Model):
	description = models.CharField(max_length=255)
	num_ordered = models.IntegerField(default=0)
	product = models.ForeignKey(Product)

	def get_amount(self, quantity):
		return self.product.price * quantity

	def __str__(self):
		return self.product.slug+" "+self.description

class ProductPhoto(models.Model):
	description = models.CharField(max_length=255)
	photo = models.ImageField(upload_to="product_photos/")
	product = models.ForeignKey(Product)

	def __str__(self):
		return self.product.slug+" "+self.description