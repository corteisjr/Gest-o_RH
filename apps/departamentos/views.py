from django.shortcuts import redirect, render
from django.views.generic import ListView
from departamentos.models import Departamento
# Listar Departamentos

class listDepartamento(ListView):
    model = Departamento
    template_name = 'departamento_list.html'
    
    # Filtracao pela empresa logada
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresas
        return Departamento.objects.filter(empresas=empresa_logada)