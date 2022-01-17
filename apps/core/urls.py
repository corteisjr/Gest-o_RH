from django.urls import path
from core.models import Channel
from apps.core.views import  homeview, indexMeeting
from agora.views import Agora

# channel=""
# app_id= '3ed0288bddd6486994871f6599c11b52'
# if Channel.objects.filter(app_id=app_id):
#     channel=Channel.objects.filter(app_id=app_id).last().channel

urlpatterns = [
    path('', homeview, name='home'),
    path("entrar", indexMeeting, name='entrar_meeting'),
    # path('meating/', Agora.as_view(app_id=app_id, channel=channel)),
]