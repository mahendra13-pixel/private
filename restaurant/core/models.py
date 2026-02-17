from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Detail(models.Model):
    name=models.CharField(max_length=50)
    phone = PhoneNumberField(region="NP")
    email=models.EmailField()
    message =models.TextField()

class Category(models.Model):
    title =models.CharField(max_length=50)
    image =models.ImageField(upload_to='category_images',null=True)
    def __str__(self):
        return self.title

class Momo(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="items")
    name = models.CharField(max_length=50)
    decs =models.TextField()
    price =models.DecimalField(max_digits=8,decimal_places=2)
    image =models.ImageField(upload_to='Momo_images')
