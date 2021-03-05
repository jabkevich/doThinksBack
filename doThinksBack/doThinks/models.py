from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    phone = models.CharField("Телефон", max_length=15, blank=True, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return self.username


class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return "пользователь: {}, Название: {}".format(self.owner, self.title)


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='task')
    title = models.CharField(max_length=50)
    deadline = models.DateTimeField(null=True)
    other = models.CharField(null=True, max_length=50)
    text = models.CharField(null=True, max_length=1000)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return "пользователь: {}, задача: {}".format(self.owner, self.title)


class Point(models.Model):
    taskFather = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="point")
    title = models.CharField(max_length=50)
    text = models.CharField(null=True, max_length=500)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return "user: {}, task: {}; задача: {}".format(self.taskFather.owner, self.taskFather, self.title)
