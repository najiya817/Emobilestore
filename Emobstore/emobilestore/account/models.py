from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustUser(AbstractUser):
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    options=(
        ("Store","Store"),
        ("Customer","Customer")
    )
    usertype=models.CharField(max_length=100,choices=options,default="Customer")

    
class products(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to="prodct_images")
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name="pro")
    wishlist_by=models.ManyToManyField(CustUser,related_name="wish",null=True)
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    def allwish(self):
        return self.wishlist_by.all()
