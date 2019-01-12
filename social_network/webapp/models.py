from django.db import models
from django.contrib.auth.models import User


class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='client', verbose_name='Пользователь')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    friends = models.ManyToManyField(User, related_name='clients_friend', verbose_name='друзья')

    def __str__(self):
        return self.user.get_full_name()


class Post(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    author = models.CharField(max_length=40, null=True, blank=True, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.title


