# Generated by Django 4.2.7 on 2023-11-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_orderсity_options_orderсity_title_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderсity',
            name='title_order',
        ),
        migrations.AddField(
            model_name='why',
            name='title_order',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок Как заказать такси внутри города?'),
        ),
    ]
