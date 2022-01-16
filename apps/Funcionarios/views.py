from django.http.response import HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import DeleteView, CreateView
from django.contrib.auth.models import User
from  Funcionarios.models import Funcionario


# Listar
class listFuncionario(ListView):
    model = Funcionario
    template_name = 'funcionario_list.html'
    # Filtração pela empresa logada
    def get_queryset(self):
        empresa_logada= self.request.user.funcionario.empresas
        queryset= Funcionario.objects.filter(empresas=empresa_logada)
        return queryset

# Actualizar
class updateFuncionario(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos', 'email']
    
# Deletar

class deleteFuncionario(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')
    
# Criar
class createFuncionario(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos', 'email']
    
    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresas = self.request.user.funcionario.empresas
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(createFuncionario, self).form_valid(form)