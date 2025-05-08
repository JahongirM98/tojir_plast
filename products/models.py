from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

LAYER_CHOICES = [
    (1, '1-слойный'),
    (2, '2-слойный'),
    (3, '3-слойный'),
]

class ProductFormType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(help_text="Объём в литрах")
    layers = models.PositiveSmallIntegerField(choices=LAYER_CHOICES)
    length = models.PositiveIntegerField(help_text="Длина в см")
    width = models.PositiveIntegerField(help_text="Ширина в см")
    height = models.PositiveIntegerField(help_text="Высота в см")
    diameter = models.PositiveIntegerField(help_text="Диаметр крышки в см")
    thickness = models.CharField(max_length=20, help_text="Толщина стенки, например '5–7 мм'")
    price = models.PositiveIntegerField(help_text="Цена в сомони")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    in_stock = models.BooleanField(default=True)
    form_type = models.ForeignKey(ProductFormType, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.volume} л)"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/gallery/')

    def __str__(self):
        return f"Фото для {self.product.name}"

class OrderRequest(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.product:
            return f"Заявка от {self.name} на {self.product.name}"
        return f"Заявка от {self.name} (без товара)"

# 🔥 Автоматическое удаление файлов при удалении объектов

@receiver(post_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)

@receiver(post_delete, sender=ProductImage)
def delete_gallery_image(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)
