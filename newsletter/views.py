from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import generics
from .serializers import SubscriptionSerializer
from .models import Subscription

class SubscriptionListCreate(generics.ListCreateAPIView):

  # The API uses ListCreateAPIView to return all the Subscription objects.
  queryset = Subscription.objects.all()
  serializer_class = SubscriptionSerializer
