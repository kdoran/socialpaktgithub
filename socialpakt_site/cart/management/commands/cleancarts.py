### -*- coding: utf-8 -*- ####################################################

import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from cart.models import Cart

class Command(BaseCommand):
    args = ''
    help = 'Deletes all old and unused carts'

    def handle(self, *args, **options):
        check_date = datetime.datetime.now() - datetime.timedelta(seconds=settings.SESSION_COOKIE_AGE)
        Cart.objects.filter(creation_date__lt=check_date).delete()
