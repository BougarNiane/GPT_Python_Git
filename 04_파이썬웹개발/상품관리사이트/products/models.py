from django.db import models


def product_image_upload_path(instance, filename):
    return f'products/{instance.code}/{filename}'


class Product(models.Model):
    image = models.ImageField(upload_to=product_image_upload_path, blank=True, null=True)
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.code} - {self.name}"
