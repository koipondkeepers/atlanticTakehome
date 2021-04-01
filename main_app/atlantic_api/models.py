from django.db import models

# Create your models here.
class Subscription(models.Model):
  id = models.CharField(max_length = 512, primary_key=True)
  plan_name = models.TextField()
  price = models.IntegerField()

class Customers(models.Model):
  id = models.CharField(max_length = 512, primary_key=True)
  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length = 100)
  address_1 = models.CharField(max_length = 100)
  address_2 = models.CharField(max_length = 100, blank=True, null=True)
  city = models.CharField(max_length = 100)
  state = models.CharField(max_length = 100)
  postal_code = models.IntegerField()
  subscription = models.ForeignKey(Subscription, on_delete = models.CASCADE)
  
class Gifts(models.Model):
  id = models.CharField(max_length = 512, primary_key=True)
  plan_name = models.TextField()
  price = models.IntegerField()
  recipient_email = models.EmailField()
  customer = models.ForeignKey(Customers,on_delete=models.CASCADE)