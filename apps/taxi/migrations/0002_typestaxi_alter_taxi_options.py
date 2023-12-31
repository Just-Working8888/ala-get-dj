# Generated by Django 4.2.7 on 2023-11-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypesTaxi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок типов такси')),
                ('descriptions', models.TextField(blank=True, null=True, verbose_name='Описание типов такси')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
            ],
            options={
                'verbose_name': 'Типы такси',
                'verbose_name_plural': 'Типы такси',
            },
        ),
        migrations.AlterModelOptions(
            name='taxi',
            options={'verbose_name': 'Настройка страницы такси', 'verbose_name_plural': 'Настройки такси'},
        ),
    ]
