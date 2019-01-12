# Generated by Django 2.1.5 on 2019-01-12 06:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_userinfo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='friends',
            field=models.ManyToManyField(related_name='clients_friend', to=settings.AUTH_USER_MODEL, verbose_name='друзья'),
        ),
    ]