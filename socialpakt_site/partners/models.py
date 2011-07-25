from django.db import models

class Partner(models.Model):
    PARTNER_TYPES = (
        ('ART', 'Artist'),
        ('NPO', 'NonProfit'),
    )

    partner_type = models.CharField(max_length=3, choices=PARTNER_TYPES, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    name = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return self.slug

class PartnerLink(models.Model):
    partner = models.ForeignKey(Partner)
    link = models.URLField()
    link_text = models.CharField(max_length=255)
    link_class = models.CharField(max_length=255)

    def __str__(self):
        return self.partner.slug+" "+self.link