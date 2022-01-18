from django.urls import path
from documentos.views import DocumentCreate


urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentCreate.as_view(), name='create_document'),
    # path('deletar/<pk>/', DocumentoDeletet.as_view(), name='delete_documento'),
]