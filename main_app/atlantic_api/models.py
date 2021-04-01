from django.db import models

# Subscriptions have a one to one relationship with customers.
class Subscription(models.Model):
  id = models.CharField(max_length = 512, primary_key=True)
  plan_name = models.TextField()
  price = models.IntegerField()

# Customers will be related one to one with subscriptions, using subscriptions as the key to map each relationship.
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
  
 # Gifts have a many to one relationship with customers, using customers as the key to map the relationship. 
class Gifts(models.Model):
  id = models.CharField(max_length = 512, primary_key=True)
  plan_name = models.TextField()
  price = models.IntegerField()
  recipient_email = models.EmailField()
  customer = models.ForeignKey(Customers,on_delete=models.CASCADE)