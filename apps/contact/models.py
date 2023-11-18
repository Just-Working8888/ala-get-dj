from django.db import models

# Create your models here.
class Contact(models.Model):
    descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание контакты',
        blank=True, null=True
    )
    banner_image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото баннера",
        blank=True, null=True
    )
    banner_image2 = models.ImageField(
        upload_to='image/',
        verbose_name="Фото баннера #2",
        blank=True, null=True
    )
    title_form = models.CharField(
        max_length=255,
        verbose_name=' Заголовок формы',
        blank=True, null=True
    )
    firstname = models.CharField(
        max_length=255,
        verbose_name='Ваше ФИО ',
        blank=True, null=True
    )
    name_company = models.CharField(
        max_length=255,
        verbose_name='Название компании ',
        blank=True, null=True
    )
    number_email = models.CharField(
        max_length=255,
        verbose_name='номер телефона/e-mail ',
        blank=True, null=True
    )

    def __str__(self):
        return str(self.descriptions) if self.descriptions else ""
    
    class Meta:
        verbose_name = 'Найстрока страницы контакты'
        verbose_name_plural = 'Найстрока страницы контакты'