# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'VariationCategory'
        db.create_table('catalog_variationcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('display_text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('exception_text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('display_order', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal('catalog', ['VariationCategory'])

        # Adding model 'ProductCategory'
        db.create_table('catalog_productcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('display_text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('display_order', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal('catalog', ['ProductCategory'])

        # Adding field 'Product.category'
        db.add_column('catalog_product', 'category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.ProductCategory'], null=True), keep_default=False)

        # Adding field 'Product.background_photo'
        db.add_column('catalog_product', 'background_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'ProductPhoto.display_order'
        db.add_column('catalog_productphoto', 'display_order', self.gf('django.db.models.fields.IntegerField')(default=-1), keep_default=False)

        # Adding field 'ProductVariation.category'
        db.add_column('catalog_productvariation', 'category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.VariationCategory'], null=True), keep_default=False)

        # Adding field 'ProductVariation.display_text'
        db.add_column('catalog_productvariation', 'display_text', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'ProductVariation.display_order'
        db.add_column('catalog_productvariation', 'display_order', self.gf('django.db.models.fields.IntegerField')(default=-1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'VariationCategory'
        db.delete_table('catalog_variationcategory')

        # Deleting model 'ProductCategory'
        db.delete_table('catalog_productcategory')

        # Deleting field 'Product.category'
        db.delete_column('catalog_product', 'category_id')

        # Deleting field 'Product.background_photo'
        db.delete_column('catalog_product', 'background_photo')

        # Deleting field 'ProductPhoto.display_order'
        db.delete_column('catalog_productphoto', 'display_order')

        # Deleting field 'ProductVariation.category'
        db.delete_column('catalog_productvariation', 'category_id')

        # Deleting field 'ProductVariation.display_text'
        db.delete_column('catalog_productvariation', 'display_text')

        # Deleting field 'ProductVariation.display_order'
        db.delete_column('catalog_productvariation', 'display_order')


    models = {
        'catalog.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'artist_on_set'", 'to': "orm['partners.Partner']"}),
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
