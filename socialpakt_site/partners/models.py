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

    image = models.ImageField(blank=True, null=True, upload_to="partner_photos/")

    def get_active_shirts(self):
        if self.partner_type == "ART":
            shirts = self.artist_on_set
        else:
            shirts = self.benefits_from_set

        return shirts.filter(active=True)

    def __str__(self):
        return self.slug

class PartnerLink(models.Model):
    partner = models.ForeignKey(Partner)
    link = models.URLField()
    link_text = models.CharField(max_length=255)
    link_class = models.CharField(max_length=255)

    def __str__(self):
        return self.partner.slug+" "+self.link