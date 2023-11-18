# Generated by Django 4.2.7 on 2023-11-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_ourmission_descriptions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='mission_descriptions_kg',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание о нас'),
        ),
        migrations.AddField(
            model_name='about',
            name='mission_descriptions_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание о нас'),
        ),
        migrations.AddField(
            model_name='about',
            name='our_mission_kg',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок о нас '),
        ),
        migrations.AddField(
            model_name='about',
            name='our_mission_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок о нас '),
        ),
        migrations.AddField(
            model_name='about',
            name='vision_descriptions_kg',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание о нас №2'),
        ),
        migrations.AddField(
            model_name='about',
            name='vision_descriptions_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание о нас №2'),
        ),
        migrations.AddField(
            model_name='about',
            name='vision_kg',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок о нас №2'),
        ),
        migrations.AddField(
            model_name='about',
            name='vision_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок о нас №2'),
        ),
        migrations.AddField(
            model_name='ourmission',
            name='descriptions2_kg',
            field=models.TextField(blank=True, null=True, verbose_name='Описание №2'),
        ),
        migrations.AddField(
            model_name='ourmission',
            name='descriptions2_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание №2'),
        ),
        migrations.AddField(
            model_name='ourmission',
            name='descriptions_kg',
            field=models.TextField(blank=True, null=True, verbose_name='Описание '),
        ),
        migrations.AddField(
            model_name='ourmission',
            name='descriptions_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание '),
        ),
        migrations.AddField(
            model_name='ourmission',
            name='title_kg',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='ourmission',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]