# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Product.donation_amount'
        db.add_column('catalog_product', 'donation_amount', self.gf('django.db.models.fields.FloatField')(default=6.0), keep_default=False)

        # Adding field 'Product.goal'
        db.add_column('catalog_product', 'goal', self.gf('django.db.models.fields.FloatField')(default=1200.0), keep_default=False)

        # Adding field 'ProductVariation.num_ordered'
        db.add_column('catalog_productvariation', 'num_ordered', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Product.donation_amount'
        db.delete_column('catalog_product', 'donation_amount')

        # Deleting field 'Product.goal'
        db.delete_column('catalog_product', 'goal')

        # Deleting field 'ProductVariation.num_ordered'
        db.delete_column('catalog_productvariation', 'num_ordered')


    models = {
        'catalog.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'artist_on_set'", 'to': "orm['partners.Partner']"}),
            'benefits': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'benefits_from_set'", 'to': "orm['partners.Partner']"}),
            'date_expires': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'donation_amount': ('django.db.models.fields.FloatField', [], {'default': '6.0'}),
            'goal': ('django.db.models.fields.FloatField', [], {'default': '1200.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_sold': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'catalog.productphoto': {
            'Meta': {'object_name': 'ProductPhoto'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Product']"})
        },
        'catalog.productvariation': {
            'Meta': {'object_name': 'ProductVariation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_ordered': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Product']"})
        },
        'partners.partner': {
            'Meta': {'object_name': 'Partner'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'partner_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['catalog']
