from django.db import models

# Create your models here.

class Subscription(models.Model):

  # A Subscription model that stores email and a name for each subscription.
  email = models.CharField(max_length=30, unique=True)
  name = models.CharField(max_length=20)
  subscribed_at = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

  def __str__(self):
    return self.email

# We could add a Newsletter model that would link with the subscription model.
# Each subscription can be for a newlsetter.