# Generated by Django 4.1.5 on 2023-01-31 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0002_alter_resto_active_alter_resto_etoiles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resto',
            old_name='PROVINCE',
            new_name='gouvernement',
        ),
        migrations.RenameField(
            model_name='resto',
            old_name='région',
            new_name='region',
        ),
    ]
