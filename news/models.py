from django.db import models


class News(models.Model):
    date = models.DateTimeField(verbose_name='Дата новости', null=False, blank=False)
    title = models.CharField(max_length=150, verbose_name='Заголовок', null=False, blank=False)
    text = models.TextField(verbose_name='Текст', null=False, blank=False)

    def __str__(self):
        return f'title: {self.title}, date: {self.date}, text: {self.text[:15]}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
