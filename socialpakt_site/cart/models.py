### -*- coding: utf-8 -*- ####################################################

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Cart(models.Model):
    creation_date = models.DateTimeField(verbose_name=_('creation date'), default=datetime.now)
    
    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = ('-creation_date',)

    def __unicode__(self):
        return unicode(self.creation_date)
    
    def get_active_items(self):
        return self.items.filter(active=True)
    
    def get_amount(self):
        return sum(item.get_amount() for item in self.get_active_items())


class ItemManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'content_object' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['content_object']))
            kwargs['object_pk'] = kwargs['content_object'].pk
            del(kwargs['content_object'])
        return super(ItemManager, self).get(*args, **kwargs)

class Item(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_('cart'), related_name="items")
    
    quantity = models.PositiveIntegerField(_('quantity'), default=1)
    
    active = models.BooleanField(_("active"), default=True)
    
    # product as generic relation
    content_type = models.ForeignKey(ContentType)
    object_pk = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_pk')

    objects = ItemManager()

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        order_with_respect_to = 'cart'
        unique_together = ('cart', 'content_type', 'object_pk')

    def __unicode__(self):
        return 'Content: %s, cart: %s' % (self.content_object, self.cart)

    def get_amount(self):
        return self.content_object.get_amount(self.quantity)
    
    def switch(self, state):
        self.active = state
        self.save()
