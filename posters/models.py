from django.db import models
from django.db.models.deletion import PROTECT

class Event(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название группы')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='posters/', null=True, verbose_name='Постер', blank=True)
    scheme = models.ImageField(upload_to='scheme/', null=True, verbose_name='Схема', blank=True)
        
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['pk']

class Session(models.Model):
    start_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата начала мероприятия')
    finish_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания мероприятия')
    title_address = models.CharField(max_length=150, blank=True, verbose_name='Место мероприятия')
    address = models.CharField(max_length=150, blank=True, verbose_name='Адрес мероприятия')
    event = models.ForeignKey(Event, null=True, on_delete=PROTECT, verbose_name='Событие')

    def __str__(self):
        return str(self.title_address)
    
    
        



class Ticket(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тип билета')
    price = models.DecimalField(max_digits=75, decimal_places=2,  verbose_name='Цена')
    event = models.ForeignKey(Event, null=True, on_delete=PROTECT, verbose_name='Событие')
    session = models.ForeignKey(Session, null=True, on_delete=PROTECT, verbose_name="Сессия")

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
    







    


