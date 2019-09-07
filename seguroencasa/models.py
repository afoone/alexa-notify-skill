from django.db import models
from rest_framework import  serializers, viewsets
from datetime import datetime, timedelta
from django.core.mail import send_mail
import pytz
import time
from rest_framework.decorators import action
from rest_framework.response import Response





# Create your models here.

class Notification(models.Model):
    time = models.PositiveSmallIntegerField()
    text = models.CharField(max_length=512)
    email = models.EmailField(max_length=254)
    email_from = models.EmailField(max_length=254)
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text + " "+ str(self.time)

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['time', 'text', 'email', 'email_from', 'sent', 'created_at']

# ViewSets define the view behavior.
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    #emailDependiente=${emailDependiente};
    @action(detail=False)
    def remove(self, request):
        email_dependiente = request.GET['emailDependiente']
        for e in Notification.objects.filter(email_from=email_dependiente):
            e.sent = True
            e.save()
        return Response(data={"msg": email_dependiente + " cancelled notifications"}, status=200)


    #emailDependiente=${emailDependiente}&emailCuidador=${emailCuidador}&mensaje=${mensaje}&minutos=${minutos}
    @action(detail=False)
    def add(self, request):
        print(request.GET)
        n = Notification()
        n.email_from=request.GET['emailDependiente']
        n.email = request.GET['emailCuidador']
        n.text = request.GET['mensaje']
        n.time = request.GET['minutos']
        n.save()
        return Response(data={"id": n.id}, status=200)


   


def sendMails():
    now = datetime.now()
    utc=pytz.UTC

    now = utc.localize(now) 
    print (now)
    time_threshold = now - timedelta(minutes = 15)
    for e in Notification.objects.all():
        time_threshold = e.created_at + timedelta(minutes = e.time)
        print("send mail "+ str(e) + " "+str(time_threshold) +" " + str(now))
        if (now > time_threshold and  not e.sent):
            print("will send mail")
            send_mail(
                'Notificación sobre el cuidado de su dependiente',
                'Su madre se ha ido a '+e.text+' a las '+str(e.created_at.hour+2)+':'+str(e.created_at.minute) +" sin haber notificado su terminación",
                'notificaciones@mifamiliaskill.com',
                [e.email],
                fail_silently=False,
            )
            time.sleep(3)
            e.sent = True
            e.save()

