# Generated by Django 4.2.7 on 2023-11-10 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_why_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='why',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Иконка'),
        ),
    ]
