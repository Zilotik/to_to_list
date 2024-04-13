from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField('Запланированное дело', max_length=100)
    description = models.TextField('Как именно делать')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/bd/{self.id}'

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Дела'