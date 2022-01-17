from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Funcionarios.models import Funcionario


@login_required
def homeview(request):
    usuario = request.user
    
    context = {
        'usuario': usuario
    }
    return render(request, template_name='home/index.html', status=200, context=context)

