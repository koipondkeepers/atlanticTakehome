from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import json
from .models import Customers, Subscription, Gifts
# Create your views here.

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