from django.db import models


class Product(models.Model):
    TYPE = {
        (0, 'Malarstwo'),
        (1, 'Ceramika'),
    }

    SOLD = {
        (0, 'Kup'),
        (1, 'Zapytaj o podobne')
    }

    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(default="")
    image = models.ImageField(upload_to="images", null=False, blank=False, default='')
    type = models.PositiveSmallIntegerField(default=0, choices=TYPE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.id} {self.title} {self.year}"

