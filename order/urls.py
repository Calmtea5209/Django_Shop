from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path('create/',order_create,name='order_create'),
]