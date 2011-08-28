# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Order'
        db.create_table('orders_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_xml', self.gf('django.db.models.fields.TextField')()),
            ('fulfilled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('orders', ['Order'])


    def backwards(self, orm):
        
        # Deleting model 'Order'
        db.delete_table('orders_order')


    models = {
        'orders.order': {
            'Meta': {'object_name': 'Order'},
            'fulfilled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_xml': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['orders']
