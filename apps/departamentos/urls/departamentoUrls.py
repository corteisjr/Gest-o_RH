from django.urls import path
from departamentos.views import listDepartamento

urlpatterns = [
    path('list', listDepartamento.as_view(), name='list_departamentos'),
]
