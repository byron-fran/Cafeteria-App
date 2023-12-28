from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Product Name")
    price = models.FloatField(verbose_name="Product Price")
    description = models.TextField(verbose_name="Product Description")
    image_url = models.FileField(max_length=200, verbose_name="Product Image Url", upload_to="products", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']
    def __str__(self):
        return self.name    