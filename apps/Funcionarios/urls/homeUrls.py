from django.urls import path
from apps.Funcionarios.views import listFuncionario, updateFuncionario

urlpatterns = [
    path(' ', listFuncionario.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', updateFuncionario.as_view(), name='update_funcionarios'),
]
