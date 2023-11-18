from django.db import models

# Create your models here.
class Delivery(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок доставки',
        blank=True, null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание доставки',
        blank=True, null=True
    )
    banner_image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото баннера",
        blank=True, null=True
    )
    trust_title = models.CharField(
        max_length=255,
        verbose_name='Заголовок доверие'
    )
    trust_descriptions = models.TextField(
        verbose_name='Описание доверие'
    )
    trust_descriptions2 = models.TextField(
        verbose_name='Описание доверие №2'
    )
    trust_image = models.ImageField(
        upload_to='image/',
        verbose_name='фото'
    )
    def __str__(self):
        return str(self.title) if self.title else ""
    
    class Meta:
        verbose_name = 'Найстрока страницы доставка'
        verbose_name_plural = 'Найстрока страницы доставка'
