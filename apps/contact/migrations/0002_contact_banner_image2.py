# Generated by Django 4.2.7 on 2023-11-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='banner_image2',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Фото баннера #2'),
        ),
    ]
