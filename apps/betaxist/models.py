from django.db import models

# Create your models here.
class Betaxist(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок стать водителем',
        blank=True, null=True
    )
    title2 = models.CharField(
        max_length=255,
        verbose_name='Заголовок стать водителем №2',
        blank=True, null=True
    )
    banner_image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото баннера",
        blank=True, null=True    
    )
    join_title = models.CharField(
        max_length=255,
        verbose_name='Заголовок присоединиться',
        blank=True, null=True
    )
    join_descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание присоединиться',
        blank=True, null=True
    )
    join_image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото присоединиться",
        blank=True, null=True    
    )
    def __str__(self):
        return str(self.title) if self.title else ""
    
    class Meta:
        verbose_name = 'Найстрока страницы стать водителем'
        verbose_name_plural = 'Найстрока страницы стать водителем'


class EarnMoney(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
        blank=True, null=True
    )
    descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание',
        blank=True, null=True
    )
    numbers = models.CharField(
        max_length=255,
        verbose_name='Номерация',
        blank=True, null=True
    )

    def __str__(self):
        return str(self.title) if self.title else ""
    
    class Meta:
        verbose_name = 'КАК ЖЕ НАЧАТЬ ЗАРАБАТЫВАТЬ С ALAGET?'
        verbose_name_plural = 'КАК ЖЕ НАЧАТЬ ЗАРАБАТЫВАТЬ С ALAGET?'