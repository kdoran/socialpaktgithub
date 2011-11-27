# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Product.has_inventory'
        db.add_column('catalog_product', 'has_inventory', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Product.has_inventory'
        db.delete_column('catalog_product', 'has_inventory')


    models = {
        'catalog.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'artist_on_set'", 'to': "orm['partners.Partner']"}),
            'benefits': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'benefits_from_set'", 'to': "orm['partners.Partner']"}),
            'call_to_action': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'cart_title': ('django.db.models.fields.CharField', [], {'default': '"This week\'s shirt"', 'max_length': '255'}),
            'date_expires': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'donation_amount': ('django.db.models.fields.FloatField', [], {'default': '6.0'}),
            'for_sale': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'goal': ('django.db.models.fields.FloatField', [], {'default': '1200.0'}),
            'has_inventory': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_sold': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'catalog.productphoto': {
            'Meta': {'object_name': 'ProductPhoto'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_large': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Product']"})
        },
        'catalog.productvariation': {
            'Meta': {'object_name': 'ProductVariation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'num_ordered': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price_override': ('django.db.models.fields.FloatField', [], {'default': '-1.0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Product']"})
        },
        'partners.partner': {
            'Meta': {'object_name': 'Partner'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'partner_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['catalog']
