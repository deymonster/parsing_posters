from django.db import models

class Posters(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название группы')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    start_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата начала мероприятия')
    finish_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания мероприятия')
    image = models.ImageField(upload_to='posters/', verbose_name='Постер', blank=True)
    scheme = models.ImageField(upload_to='scheme/', verbose_name='Схема', blank=True)
    title_address = models.CharField(max_length=150, blank=True, verbose_name='Название места мероприятия')
    address = models.CharField(max_length=150, blank=True, verbose_name='Адрес мероприятия')
    ticket_type = models.ForeignKey('Ticket', on_delete=models.PROTECT, null=True, verbose_name='Билет и цена')




    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Постер'
        verbose_name_plural = 'Постеры'
        ordering = ['pk']


class Ticket(models.Model):
    ticket_title = models.CharField(max_length=150, verbose_name='Тип билета')
    ticket_price = models.PositiveSmallIntegerField(verbose_name='Цена')

    def __str__(self):
        return self.ticket_title

    


