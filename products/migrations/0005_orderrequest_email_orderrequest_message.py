# Generated by Django 4.2.11 on 2025-04-24 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrequest',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='orderrequest',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
