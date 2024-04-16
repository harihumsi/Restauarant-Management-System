from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length= 50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    content = models.TextField()
    
    def __str__(self) -> str:
        return 'Message from '+self.name
    
class Order(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    item_name = models.CharField(max_length=50)
    item_quantity = models.IntegerField()
    
    def __str__(self) -> str:
        return "Order for table number" + str(self.number)
    
class Food_Item(models.Model):
    name = models.CharField(max_length=30)
    item_price = models.CharField(max_length=20)
    link = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.name
    
class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    
    def __str__(self) -> str:
        return self.name + "'s review"
    
# Create your models here.
