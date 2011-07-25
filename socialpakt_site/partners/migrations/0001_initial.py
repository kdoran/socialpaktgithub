# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Partner'
        db.create_table('partners_partner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('partner_type', self.gf('django.db.models.fields.CharField')(max_length=3, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('about', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('partners', ['Partner'])

        # Adding model 'PartnerLink'
        db.create_table('partners_partnerlink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['partners.Partner'])),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('link_text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link_class', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('partners', ['PartnerLink'])


    def backwards(self, orm):
        
        # Deleting model 'Partner'
        db.delete_table('partners_partner')

        # Deleting model 'PartnerLink'
        db.delete_table('partners_partnerlink')


    models = {
        'partners.partner': {
            'Meta': {'object_name': 'Partner'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'partner_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'partners.partnerlink': {
            'Meta': {'object_name': 'PartnerLink'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'link_class': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['partners.Partner']"})
        }
    }

    complete_apps = ['partners']
