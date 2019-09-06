from django.db import models
from rest_framework import  serializers, viewsets






# Create your models here.

class Notification(models.Model):
    time = models.DateTimeField()
    text = models.CharField(max_length=512)
    email = models.EmailField(max_length=254) 
    def __str__(self):
        return self.text

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['time', 'text', 'email']

# ViewSets define the view behavior.
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
