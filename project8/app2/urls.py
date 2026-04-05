from django.urls import path
from app2.views import *
urlpatterns = [
    path('akash/',akash,name='akash'),
]