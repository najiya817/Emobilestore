# Generated by Django 4.1.7 on 2023-04-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_delete_addtocart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='image',
            field=models.ImageField(null=True, upload_to='prodct_images'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
