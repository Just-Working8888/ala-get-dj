# Generated by Django 4.2.7 on 2023-11-10 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_slider_remove_settings_image_slider_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Why',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('descriptions', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Почему Alaget?',
                'verbose_name_plural': 'Почему Alaget?',
            },
        ),
        migrations.AlterField(
            model_name='slider',
            name='descriptions',
            field=models.TextField(blank=True, null=True, verbose_name='Описание слайлера'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image_slider',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Фото слайдера'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='numbering',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Номерация слайдера'),
        ),
    ]