# Generated by Django 4.2.7 on 2023-11-10 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_index_title2_alter_index_banner_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='banner_image2',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Фото баннера2'),
        ),
    ]