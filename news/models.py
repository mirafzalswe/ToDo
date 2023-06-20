from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField('name', max_length=200)
    name_task = models.CharField('name_task', max_length=200)
    task_txt = models.TextField('task_text', max_length=2000)
    date = models.DateTimeField('time')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/news/{self.id}/'

