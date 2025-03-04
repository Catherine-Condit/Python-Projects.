from email.policy import default

from django.db import models

# Create your models here.
TYPE_CHOICES = {
    ('appetizers', 'appetizers'),
    ('entrees', 'entrees'),
    ('treats', 'treats'),
    ('drinks', 'drinks'),
}

# schema for products
class Product(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    # blank=True is for forms on actual webpage, but they eventually will need to bc null=False means db will not save an empty space/field.
    description = models.TextField(max_length=300, default="", blank=True)
    price = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    image = models.CharField(max_length=255, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
    #turns "product object" nondescript name to a name that is readable to users