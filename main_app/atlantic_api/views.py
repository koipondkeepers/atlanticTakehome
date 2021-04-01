from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import json
from .models import Customers, Subscription, Gifts

# Allows the user to submit the JSON object for inserting into our DB.
# We receive the json object and decode it.
# We create the subscription object first before we can use it to create a record of the customer.
# Gifts are iterable, so a new row must be made per gift.
class Submit(APIView):
  def post(self, request, *args, **kwargs):
    body = json.loads(request.body.decode('utf-8'))
    customer_data = body.pop('customer')
    gifts_data = customer_data.pop('gifts')
    subscription_data = customer_data.pop('subscription')
    subscription = Subscription.objects.create(**subscription_data)
    customer = Customers.objects.create(subscription=subscription, **customer_data)
    for gift_data in gifts_data:
      Gifts.objects.create(customer=customer, **gift_data)
    customer.save()
    return JsonResponse({
      'response': 200,
      'message' : 'Successfully Submitted'
    })

class Update(APIView):
  def post(self, request, *args, **kwargs):
    body = json.loads(request.body.decode('utf-8'))
    new_customer_data = body.pop('customer')
    new_gifts_data = new_customer_data.pop('gifts')
    new_subscription_data = new_customer_data.pop('subscription')
    subscription = get_object_or_404(Subscription, id=new_subscription_data['id'])
    subscription.plan_name = new_subscription_data['plan_name']
    subscription.price = new_subscription_data['price']
    subscription.save()
    customer = get_object_or_404(Customers, id=new_customer_data['id'])
    customer.first_name = new_customer_data['first_name']
    customer.last_name = new_customer_data['last_name']
    customer.address_1 = new_customer_data['address_1']
    customer.address_2 = new_customer_data['address_2']
    customer.city = new_customer_data['city']
    customer.state = new_customer_data['state']
    customer.postal_code = new_customer_data['postal_code']
    customer.subscription = subscription
    customer.save()
    for new_gift in new_gifts_data:
      if Gifts.objects.filter(id=new_gift['id']).exists():
        gift = Gifts.objects.get(id=new_gift['id'])
        gift.plan_name = new_gift['plan_name']
        gift.price = new_gift['price']
        gift.recipient_email = new_gift['recipient_email']
        gift.save()
      else:
        Gifts.objects.create(customer=customer, **new_gift)
    return JsonResponse({
      'response': 200,
      'message' : f'Successfully updated',
    })