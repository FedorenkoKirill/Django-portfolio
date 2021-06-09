from django.db import models

class Blog(models.Model):
    title = models.CharField('Тема', max_length = 255)
    text = models.TextField('Содержание')

    def __str__(self):
        return self.title