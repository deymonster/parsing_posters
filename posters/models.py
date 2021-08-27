from django.db import models

class Posters(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название группы')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    start_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата начала мероприятия')
    finish_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания мероприятия')
    image = models.ImageField(upload_to='posters/', verbose_name='Постер', blank=True)
    #scheme = models.ImageField(upload_to='scheme/', verbose_name='Схема', blank=True)
    #title_address = models.CharField(max_length=150, verbose_name='Название места мероприятия')
    #address = models.CharField(max_length=150, verbose_name='Адрес мероприятия')



    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Постер'
        verbose_name_plural = 'Постеры'
        ordering = ['pk']
