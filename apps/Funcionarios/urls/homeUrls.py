from django.urls import path
from apps.Funcionarios.views import funcionariosView

urlpatterns = [
    path('', funcionariosView, name='funcionarios')
]
