from django import template

register = template.Library()

@register.simple_tag
def product_stock(variations, variation_name):
	variation = variations.filter(description=variation_name)
	if len(variation):
		v = variation[0]
		if v.inventory < 0:
			return str(v.inventory) if not v.product.has_inventory else "0"
		
		return str(v.inventory)
	
	return "0"