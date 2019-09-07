from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail
from .models import Notification, sendMails



class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every one minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code


    def querySet_to_list(qs):
        return [dict(q) for q in qs]

    def do(self):
        print("comprobando elementos")
        sendMails()
        # hora de ahora
        # notifications_set = getObjects()
        # print("notification set")
        # print (notifications_set)
        # print(querySet_to_list(notifications_set))
        # for notification in notifications_set:
        #     print(notification)
        #     # time_threshold = notification.created_at + timedelta(minutes=notification.time)
        #     # print(time_threshold)           
            # if (now > obj.created_at):
            #     print("send mail")
            #     send_mail(
            #         'Notificación sobre el cuidado de su dependiente',
            #         'Su madre se ha ido a '+obj.text+' a las '+obj.time.hour+':'+obj.time.minutes +" sin haber notificado su terminación",
            #         'notificaciones@mifamiliaskill.com',
            #         [],
            #         fail_silently=False,
            #     )
            #     obj.sent = True
            #     obj.save()