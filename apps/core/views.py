from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def homeview(request):
    return render(request, template_name='home/index.html', status=200)