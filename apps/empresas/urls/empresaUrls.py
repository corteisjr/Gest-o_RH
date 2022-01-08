from django.urls import path
from apps.empresas.views import EmpresaCreate 

urlpatterns = [
    path('nova', EmpresaCreate.as_view(), name='create_empresa')
]