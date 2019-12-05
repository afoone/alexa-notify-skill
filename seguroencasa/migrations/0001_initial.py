# Generated by Django 2.2.5 on 2019-09-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('text', models.CharField(max_length=512)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]