from unicodedata import name
from django.urls import path
from departamentos.views import DeleteDepartamento, listDepartamento, updadeDepartamento, CreateDepartamento

urlpatterns = [
    path('list', listDepartamento.as_view(), name='list_departamentos'),
    path('novo/', CreateDepartamento.as_view(), name='new_departamentos'),
    path('edit/<int:pk>/', updadeDepartamento.as_view(), name='update_departamentos'),
    path('delete/<int:pk>/', DeleteDepartamento.as_view(), name='delete_departamentos')
]
