from django.urls import include, path

from . import views

urlpatterns = [
  
  path('api', views.SubscriptionListCreate.as_view() ),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]