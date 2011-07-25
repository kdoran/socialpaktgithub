# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Product'
        db.create_table('catalog_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_expires', self.gf('django.db.models.fields.DateTimeField')()),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='artist_on_set', to=orm['partners.Partner'])),
            ('benefits', self.gf('django.db.models.fields.related.ForeignKey')(related_name='benefits_from_set', to=orm['partners.Partner'])),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('total_sold', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('catalog', ['Product'])

        # Adding model 'ProductVariation'
        db.create_table('catalog_productvariation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Product'])),
        ))
        db.send_create_signal('catalog', ['ProductVariation'])

        # Adding model 'ProductPhoto'
        db.create_table('catalog_productphoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Product'])),
        ))
        db.send_create_signal('catalog', ['ProductPhoto'])


    def backwards(self, orm):
        
        # Deleting model 'Product'
        db.delete_table('catalog_product')

        # Deleting model 'ProductVariation'
        db.delete_table('catalog_productvariation')

        # Deleting model 'ProductPhoto'
        db.delete_table('catalog_productphoto')


    models = {
        'catalog.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'artist_on_set'", 'to': "orm['partners.Partner']"}),
            'benefits': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'benefits_from_set'", 'to': "orm['partners.Partner']"}),
            'date_expires': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
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
