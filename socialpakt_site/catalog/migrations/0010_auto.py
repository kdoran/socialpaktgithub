# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field available_variations on 'Product'
        db.create_table('catalog_product_available_variations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['catalog.product'], null=False)),
            ('variationcategory', models.ForeignKey(orm['catalog.variationcategory'], null=False))
        ))
        db.create_unique('catalog_product_available_variations', ['product_id', 'variationcategory_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field available_variations on 'Product'
        db.delete_table('catalog_product_available_variations')


    models = {
        'catalog.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'artist_on_set'", 'to': "orm['partners.Partner']"}),
            'available_variations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.VariationCategory']", 'null': 'True', 'symmetrical': 'False'}),
            'background_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'benefits': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'benefits_from_set'", 'to': "orm['partners.Partner']"}),
            'call_to_action': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'cart_title': ('django.db.models.fields.CharField', [], {'default': '"This week\'s shirt"', 'max_length': '255'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.ProductCategory']", 'null': 'True'}),
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
        'catalog.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'display_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'catalog.productphoto': {
            'Meta': {'object_name': 'ProductPhoto'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_large': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Product']"})
        },
        'catalog.productvariation': {
            'Meta': {'object_name': 'ProductVariation'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.VariationCategory']", 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'display_text': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'num_ordered': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price_override': ('django.db.models.fields.FloatField', [], {'default': '-1.0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Product']"})
        },
        'catalog.variationcategory': {
            'Meta': {'object_name': 'VariationCategory'},
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'display_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'exception_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
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
