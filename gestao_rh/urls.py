from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include


urlpatterns = [
    path('', include('apps.core.urls')),
    path('funcionarios/', include('apps.Funcionarios.urls.homeUrls')),
    path('departamentos/', include('apps.departamentos.urls.departamentoUrls')),
    path('documentos/', include('apps.documentos.urls.documentoUrls')),
    path('empresa/', include('apps.empresas.urls.empresaUrls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
