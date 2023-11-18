from django.db import models

# Create your models here.
class Partners(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок партнерство',
        blank=True, null=True
    )
    title2 = models.CharField(
        max_length=255,
        verbose_name='Заголовок партнерство',
        blank=True, null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание партнерство',
        blank=True, null=True
    )
    banner_image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото баннера",
        blank=True, null=True
    )
    become_title = models.CharField(
        max_length=255,
        verbose_name='Заголовок СТАТЬ ПАРТНЕРОМ ',
        blank=True, null=True
    )
    become_descriptions = models.TextField(
        verbose_name='Описание СТАТЬ ПАРТНЕРОМ ',
        blank=True, null=True
    )
    become_image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото СТАТЬ ПАРТНЕРОМ ",
        blank=True, null=True
    )
    
    local_title = models.CharField(
        max_length=255,
        verbose_name='Заголовок Локальный таксопарк',
        blank=True, null=True
    )
    local_title2 = models.CharField(
        max_length=255,
        verbose_name='Заголовок Локальный таксопарк',
        blank=True, null=True
    )
    local_descriptions = models.TextField(
        verbose_name='Описание Локальный таксопарк',
        blank=True, null=True
    )
    getting_title = models.CharField(
        max_length=255,
        verbose_name='Заголовок Что вы получаете',
        blank=True, null=True
    )
    getting_descriptions = models.TextField(
        verbose_name='Описание Что вы получаете',
        blank=True, null=True
    )
    getting_descriptions2 = models.TextField(
        verbose_name='Описание Что вы получаете',
        blank=True, null=True
    )
    getting_descriptions3 = models.TextField(
        verbose_name='Описание Что вы получаете',
        blank=True, null=True
    )
    def __str__(self):
        return str(self.title) if self.title else ""
    
    class Meta:
        verbose_name = 'Найстрока страницы партнерство'
        verbose_name_plural = 'Найстрока страницы партнерство'


class   LocalTaxi(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок партнерство',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото',
        blank=True, null=True
    )
    def __str__(self):
        return str(self.title) if self.title else ""
    
    class Meta:
        verbose_name = 'Этапы партнерство'
        verbose_name_plural = 'Этапы партнерство'


class PartnersSlider(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name='Название',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото',
        blank=True, null=True
    )


    def __str__(self):
        return str(self.title) if self.title else ""
    
    class Meta:
        verbose_name = 'Слайдер партерство'
        verbose_name_plural = 'Слайдер партерство'
