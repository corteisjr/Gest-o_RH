from django.urls import path
from apps.Funcionarios.views import (
    listFuncionario, 
    updateFuncionario, 
    deleteFuncionario, 
    createFuncionario
)


urlpatterns = [
    path(' ', listFuncionario.as_view(), name='list_funcionarios'),
    path('novo/', createFuncionario.as_view(), name='create_funcionario'),
    path('editar/<int:pk>', updateFuncionario.as_view(), name='update_funcionarios'),
    path('delete/<int:pk>', deleteFuncionario.as_view(), name='delete_funcionarios'),
]
