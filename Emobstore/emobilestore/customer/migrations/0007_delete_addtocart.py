# Generated by Django 4.1.7 on 2023-04-18 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_addtocart_product_alter_cartitem_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddToCart',
        ),
    ]
