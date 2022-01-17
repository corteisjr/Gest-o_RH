from django.db import models


class Meeting(models.Model):
    channel = models.TextField()
    meeting_title = models.CharField(max_length=50)
    meeting_subject = models.CharField(max_length=100)
    start_time = models.TimeField(auto_now=True)
    end_time = models.TimeField(auto_now_add=True)
    date = models.DateTimeField()
    
class Channel(models.Model):
    channel = models.CharField(max_length=50)
    app_id = models.TextField()