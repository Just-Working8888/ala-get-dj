# Generated by Django 4.2.7 on 2023-11-12 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_about_mission_descriptions_kg_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='mission_descriptions_kg',
            new_name='mission_descriptions_ky',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='our_mission_kg',
            new_name='our_mission_ky',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='vision_descriptions_kg',
            new_name='vision_descriptions_ky',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='vision_kg',
            new_name='vision_ky',
        ),
        migrations.RenameField(
            model_name='ourmission',
            old_name='descriptions2_kg',
            new_name='descriptions2_ky',
        ),
        migrations.RenameField(
            model_name='ourmission',
            old_name='descriptions_kg',
            new_name='descriptions_ky',
        ),
        migrations.RenameField(
            model_name='ourmission',
            old_name='title_kg',
            new_name='title_ky',
        ),
    ]
