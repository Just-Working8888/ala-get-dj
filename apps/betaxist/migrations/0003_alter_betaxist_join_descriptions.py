# Generated by Django 4.2.7 on 2023-11-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betaxist', '0002_remove_betaxist_descriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betaxist',
            name='join_descriptions',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание присоединиться'),
        ),
    ]