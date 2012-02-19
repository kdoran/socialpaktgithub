from django.db import models

from partners.models import Partner

class ProductCategory(models.Model):

	slug = models.SlugField(max_length=255, db_index=True)
	display_text = models.CharField(max_length=255)
	display_order = models.IntegerField(default=-1)

	def __str__(self):
		return self.slug

class HomeCategory(models.Model):

	slug = models.SlugField(max_length=255, db_index=True)
	display_text = models.CharField(max_length=255)
	category = models.ForeignKey(ProductCategory, null=True, blank=True)

	def __str__(self):
		return self.slug

class VariationCategory(models.Model):
	
	slug = models.SlugField(max_length=255, db_index=True)
	display_text = models.CharField(max_length=255)
	exception_text = models.CharField(max_length=255, blank=True)
	display_order = models.IntegerField(default=-1)

	def __str__(self):
		return self.slug

class Product(models.Model):
	"""Model representing a tshirt for SocialPakt"""

	category = models.ForeignKey(ProductCategory, null=True)
	featured = models.BooleanField(default=False)
	available_variations = models.ManyToManyField(VariationCategory, null=True)
	background_photo = models.ImageField(upload_to="product_photos/", null=True, blank=True)

	slug = models.SlugField(max_length=255, db_index=True)
	title = models.CharField(max_length=255)
	cart_title = models.CharField(max_length=255, default="This week's shirt")
	description = models.TextField()
	call_to_action = models.CharField(max_length=255, default="")

	active = models.BooleanField(default=False, db_index=True)
	date_expires = models.DateTimeField(db_index=True)

	for_sale = models.BooleanField(default=True)
	has_inventory = models.BooleanField(default=False)

	artist = models.ForeignKey(Partner, related_name="artist_on_set")
	benefits = models.ForeignKey(Partner, related_name="benefits_from_set")

	price = models.FloatField()
	donation_amount = models.FloatField(default=6.0)
	goal = models.FloatField(default=1200.0)
	total_sold = models.IntegerField(default=0)

	votes = models.IntegerField(default=0)

	def total_raised(self):
		return self.total_sold*self.donation_amount

	def distance_to_goal(self):
		return self.total_raised() / self.goal * 100.0

	# mark other products for this cat
	# not sure if there's a better way to do this
	# http://stackoverflow.com/questions/9237003/one-to-one-and-one-to-many-modeling
	def save(self, *args, **kwargs):
		if (self.featured):
			for product in Product.objects.filter(category=self.category):
				product.featured = False
				product.save()
			self.featured = True
		super(Product, self).save(*args, **kwargs)

	def __str__(self):
		return self.slug
		
class ProductVariation(models.Model):
	category = models.ForeignKey(VariationCategory, null=True)
	description = models.CharField(max_length=255)
	display_text = models.CharField(max_length=255, default="", blank=True)
	display_order = models.IntegerField(default=-1)
	num_ordered = models.IntegerField(default=0)
	product = models.ForeignKey(Product)

	inventory = models.IntegerField(default = -1)
	price_override = models.FloatField(default = -1.0)

	def get_amount(self, quantity):
		price = self.price_override if self.price_override >= 0.0 else self.product.price
		return price * quantity

	def __str__(self):
		return self.product.slug+" "+self.description

class ProductPhoto(models.Model):
	description = models.CharField(max_length=255)
	display_order = models.IntegerField(default=-1)
	photo = models.ImageField(upload_to="product_photos/")
	photo_large = models.ImageField(upload_to="product_photos/", blank=True, null=True)

	product = models.ForeignKey(Product)

	def __str__(self):
		return self.product.slug+" "+self.description

class CatalogGlobals(models.Model):
	global_set = models.SlugField(max_length=255, db_index=True)
	default_category = models.ForeignKey(ProductCategory)