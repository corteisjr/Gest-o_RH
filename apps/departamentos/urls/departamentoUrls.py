from unicodedata import name
from django.urls import path
from departamentos.views import listDepartamento, updadeDepartamento

urlpatterns = [
    path('list', listDepartamento.as_view(), name='list_departamentos'),
    path('edit/<int:pk>/', updadeDepartamento.as_view(), name='update_departamentos')
]
