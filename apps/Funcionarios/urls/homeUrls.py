from django.urls import path
from apps.Funcionarios.views import listFuncionario

urlpatterns = [
    path(' ', listFuncionario.as_view(), name='list_funcionarios'),
]
