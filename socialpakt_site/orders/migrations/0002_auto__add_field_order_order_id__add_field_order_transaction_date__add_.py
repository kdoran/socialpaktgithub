# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Order.order_id'
        db.add_column('orders_order', 'order_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.transaction_date'
        db.add_column('orders_order', 'transaction_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'Order.processor_response'
        db.add_column('orders_order', 'processor_response', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_id'
        db.add_column('orders_order', 'customer_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.is_anonymous'
        db.add_column('orders_order', 'is_anonymous', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_first_name'
        db.add_column('orders_order', 'customer_first_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_last_name'
        db.add_column('orders_order', 'customer_last_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_company'
        db.add_column('orders_order', 'customer_company', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_address1'
        db.add_column('orders_order', 'customer_address1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_address2'
        db.add_column('orders_order', 'customer_address2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_city'
        db.add_column('orders_order', 'customer_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_state'
        db.add_column('orders_order', 'customer_state', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_postal_code'
        db.add_column('orders_order', 'customer_postal_code', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_country'
        db.add_column('orders_order', 'customer_country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_phone'
        db.add_column('orders_order', 'customer_phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_email'
        db.add_column('orders_order', 'customer_email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_ip'
        db.add_column('orders_order', 'customer_ip', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.shipping_first_name'
        db.add_column('orders_order', 'shipping_first_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.shipping_last_name'
        db.add_column('orders_order', 'shipping_last_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.shipping_company'
        db.add_column('orders_order', 'shipping_company', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.shipping_address1'
        db.add_column('orders_order', 'shipping_address1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.shipping_address2'
        db.add_column('orders_order', 'shipping_address2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.shipping_city'
        db.add_column('orders_order', 'shipping_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.shipping_state'
        db.add_column('orders_order', 'shipping_state', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.shipping_postal_code'
        db.add_column('orders_order', 'shipping_postal_code', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.shipping_country'
        db.add_column('orders_order', 'shipping_country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.shipping_phone'
        db.add_column('orders_order', 'shipping_phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.shipto_shipping_service_description'
        db.add_column('orders_order', 'shipto_shipping_service_description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.purchase_order'
        db.add_column('orders_order', 'purchase_order', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.cc_number_masked'
        db.add_column('orders_order', 'cc_number_masked', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.cc_type'
        db.add_column('orders_order', 'cc_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.cc_exp_month'
        db.add_column('orders_order', 'cc_exp_month', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.cc_exp_year'
        db.add_column('orders_order', 'cc_exp_year', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.product_total'
        db.add_column('orders_order', 'product_total', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.tax_total'
        db.add_column('orders_order', 'tax_total', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.shipping_total'
        db.add_column('orders_order', 'shipping_total', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.order_total'
        db.add_column('orders_order', 'order_total', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.payment_gateway_type'
        db.add_column('orders_order', 'payment_gateway_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.receipt_url'
        db.add_column('orders_order', 'receipt_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.taxes'
        db.add_column('orders_order', 'taxes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.discounts'
        db.add_column('orders_order', 'discounts', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_password'
        db.add_column('orders_order', 'customer_password', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_password_salt'
        db.add_column('orders_order', 'customer_password_salt', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_password_hash_type'
        db.add_column('orders_order', 'customer_password_hash_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.customer_password_hash_config'
        db.add_column('orders_order', 'customer_password_hash_config', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Order.items_ordered'
        db.add_column('orders_order', 'items_ordered', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Order.order_id'
        db.delete_column('orders_order', 'order_id')

        # Deleting field 'Order.transaction_date'
        db.delete_column('orders_order', 'transaction_date')

        # Deleting field 'Order.processor_response'
        db.delete_column('orders_order', 'processor_response')

        # Deleting field 'Order.customer_id'
        db.delete_column('orders_order', 'customer_id')

        # Deleting field 'Order.is_anonymous'
        db.delete_column('orders_order', 'is_anonymous')

        # Deleting field 'Order.customer_first_name'
        db.delete_column('orders_order', 'customer_first_name')

        # Deleting field 'Order.customer_last_name'
        db.delete_column('orders_order', 'customer_last_name')

        # Deleting field 'Order.customer_company'
        db.delete_column('orders_order', 'customer_company')

        # Deleting field 'Order.customer_address1'
        db.delete_column('orders_order', 'customer_address1')

        # Deleting field 'Order.customer_address2'
        db.delete_column('orders_order', 'customer_address2')

        # Deleting field 'Order.customer_city'
        db.delete_column('orders_order', 'customer_city')

        # Deleting field 'Order.customer_state'
        db.delete_column('orders_order', 'customer_state')

        # Deleting field 'Order.customer_postal_code'
        db.delete_column('orders_order', 'customer_postal_code')

        # Deleting field 'Order.customer_country'
        db.delete_column('orders_order', 'customer_country')

        # Deleting field 'Order.customer_phone'
        db.delete_column('orders_order', 'customer_phone')

        # Deleting field 'Order.customer_email'
        db.delete_column('orders_order', 'customer_email')

        # Deleting field 'Order.customer_ip'
        db.delete_column('orders_order', 'customer_ip')

        # Deleting field 'Order.shipping_first_name'
        db.delete_column('orders_order', 'shipping_first_name')

        # Deleting field 'Order.shipping_last_name'
        db.delete_column('orders_order', 'shipping_last_name')

        # Deleting field 'Order.shipping_company'
        db.delete_column('orders_order', 'shipping_company')

        # Deleting field 'Order.shipping_address1'
        db.delete_column('orders_order', 'shipping_address1')

        # Deleting field 'Order.shipping_address2'
        db.delete_column('orders_order', 'shipping_address2')

        # Deleting field 'Order.shipping_city'
        db.delete_column('orders_order', 'shipping_city')

        # Deleting field 'Order.shipping_state'
        db.delete_column('orders_order', 'shipping_state')

        # Deleting field 'Order.shipping_postal_code'
        db.delete_column('orders_order', 'shipping_postal_code')

        # Deleting field 'Order.shipping_country'
        db.delete_column('orders_order', 'shipping_country')

        # Deleting field 'Order.shipping_phone'
        db.delete_column('orders_order', 'shipping_phone')

        # Deleting field 'Order.shipto_shipping_service_description'
        db.delete_column('orders_order', 'shipto_shipping_service_description')

        # Deleting field 'Order.purchase_order'
        db.delete_column('orders_order', 'purchase_order')

        # Deleting field 'Order.cc_number_masked'
        db.delete_column('orders_order', 'cc_number_masked')

        # Deleting field 'Order.cc_type'
        db.delete_column('orders_order', 'cc_type')

        # Deleting field 'Order.cc_exp_month'
        db.delete_column('orders_order', 'cc_exp_month')

        # Deleting field 'Order.cc_exp_year'
        db.delete_column('orders_order', 'cc_exp_year')

        # Deleting field 'Order.product_total'
        db.delete_column('orders_order', 'product_total')

        # Deleting field 'Order.tax_total'
        db.delete_column('orders_order', 'tax_total')

        # Deleting field 'Order.shipping_total'
        db.delete_column('orders_order', 'shipping_total')

        # Deleting field 'Order.order_total'
        db.delete_column('orders_order', 'order_total')

        # Deleting field 'Order.payment_gateway_type'
        db.delete_column('orders_order', 'payment_gateway_type')

        # Deleting field 'Order.receipt_url'
        db.delete_column('orders_order', 'receipt_url')

        # Deleting field 'Order.taxes'
        db.delete_column('orders_order', 'taxes')

        # Deleting field 'Order.discounts'
        db.delete_column('orders_order', 'discounts')

        # Deleting field 'Order.customer_password'
        db.delete_column('orders_order', 'customer_password')

        # Deleting field 'Order.customer_password_salt'
        db.delete_column('orders_order', 'customer_password_salt')

        # Deleting field 'Order.customer_password_hash_type'
        db.delete_column('orders_order', 'customer_password_hash_type')

        # Deleting field 'Order.customer_password_hash_config'
        db.delete_column('orders_order', 'customer_password_hash_config')

        # Deleting field 'Order.items_ordered'
        db.delete_column('orders_order', 'items_ordered')


    models = {
        'orders.order': {
            'Meta': {'object_name': 'Order'},
            'cc_exp_month': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cc_exp_year': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cc_number_masked': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cc_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_password_hash_config': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_password_hash_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_password_salt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customer_state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'discounts': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fulfilled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_anonymous': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'items_ordered': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'order_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order_total': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order_xml': ('django.db.models.fields.TextField', [], {}),
            'payment_gateway_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'processor_response': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_total': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'purchase_order': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'receipt_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipping_total': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shipto_shipping_service_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tax_total': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'taxes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'transaction_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['orders']
