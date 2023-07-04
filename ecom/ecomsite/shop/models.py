from django.db import models

# Create your models here.
class Products(models.Model):
    title= models.CharField(max_length=200,null=True)
    price= models.FloatField(null=True)
    discounted_price= models.FloatField(null=True)
    category= models.CharField(max_length=200,default='DEFAULT VALUE',null=True)
    description= models.TextField(null=True)
    image= models.CharField(max_length=400,null=True)
    # we use charField ,because we want to store images url ,because images can be store at different servers, so we basically refer that to our website

    # def __str__(self):
    #     return self.title
    
class Order(models.Model):
    items=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zipcode=models.CharField(max_length=200)
    total=models.CharField(max_length=200)
