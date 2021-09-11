# Generated by Django 3.2.6 on 2021-08-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0002_auto_20210827_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posters',
            name='scheme',
        ),
        migrations.AddField(
            model_name='posters',
            name='ticket_price',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='posters',
            name='ticket_type',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Тип билета'),
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]