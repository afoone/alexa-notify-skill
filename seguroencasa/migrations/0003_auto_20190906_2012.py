# Generated by Django 2.2.5 on 2019-09-06 20:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('seguroencasa', '0002_notification_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
