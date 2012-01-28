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

@register.inclusion_tag("catalog/product_variations.html")
def render_variations(cat, product):
	variations = product.productvariation_set.filter(category=cat)
	if product.has_inventory:
		variations = variations.filter(inventory__gt=0)

	return { "variations" : variations.order_by('display_order') }
