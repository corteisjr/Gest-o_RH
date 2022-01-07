from django.urls import path
from apps.core.views import  homeview

urlpatterns = [
    path('', homeview, name='home')
]