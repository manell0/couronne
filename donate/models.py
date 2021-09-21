from django.db import models


# The stripe model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents
    file = models.FileField(upload_to="product_files/", blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return self.name

    # Format the price out put
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
