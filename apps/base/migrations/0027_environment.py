# Generated by Django 4.2.7 on 2023-11-12 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_base'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='ПАРТНЕРСТВО')),
                ('title_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='ПАРТНЕРСТВО')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='ПАРТНЕРСТВО')),
                ('descriptions', models.CharField(blank=True, max_length=255, null=True, verbose_name='Footer text')),
                ('descriptions_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='Footer text')),
                ('descriptions_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Footer text')),
                ('descriptions2', models.CharField(blank=True, max_length=255, null=True, verbose_name='ПАРТНЕРСТВО')),
                ('descriptions2_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='ПАРТНЕРСТВО')),
                ('descriptions2_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='ПАРТНЕРСТВО')),
                ('descriptions3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Footer text')),
                ('descriptions3_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='Footer text')),
                ('descriptions3_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Footer text')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'За экологию Кыргызстана',
                'verbose_name_plural': 'За экологию Кыргызстана',
            },
        ),
    ]
