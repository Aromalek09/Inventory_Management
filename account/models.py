from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Products(models.Model):
    ProductID=models.BigIntegerField(unique=True)    
    ProductCode=models.CharField(max_length=255, unique=True)
    ProductName=models.CharField(max_length=255)    
    ProductImage=models.ImageField(upload_to="product_images")
    CreatedDate=models.DateTimeField(auto_now_add=True)
    UpdatedDate=models.DateTimeField(blank=True, null=True)
    CreatedUser=models.ForeignKey(User,on_delete=models.CASCADE)   
    IsFavourite=models.BooleanField(default=False)
    Active=models.BooleanField(default=True)    
    HSNCode=models.CharField(max_length=255, blank=True, null=True)
    TotalStock = models.DecimalField(default=0.00, max_digits=20, decimal_places=8, blank=True, null=True)
    options=(
        ("Shirt","Shirt"),
        ("pant","pant"),
        ("Saree","Saree"),
        ("Kurta","Kurta"),
        ("Gown","Gown"),
        
    )
    category=models.CharField(max_length=100,choices=options)
    

class Cart(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    options=(
        ("M","M"),
        ("L","L"),
        ("S","S"),
    )
    size=models.CharField(max_length=100,choices=options)
    
    optionss=(
        ("Red","Red"),
        ("Blue","Blue"),
        ("Black","Black"),
    )
    colours=models.CharField(max_length=100,choices=optionss)
    
class Orders(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("OrderPlaced","OrderPlaced"),
        ("Shipped","Shipped"),
        ("OutForDelivery","OutForDelivery"),
        ("Delivered","Delivered"),
        ("Cancelled","Cancelled"),
        
    )
    
    status=models.CharField(max_length=100,default="OrderPlaced",choices=options)


