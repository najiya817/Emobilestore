# Generated by Django 4.1.7 on 2023-04-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_cartitem_image_cartitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='image',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]