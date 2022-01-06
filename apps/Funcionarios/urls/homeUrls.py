from django.urls import path
from apps.Funcionarios.views import homeView

urlpatterns = [
    path('', homeView, name='home')
]
