# Generated by Django 4.1.5 on 2023-02-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0006_remove_commantair_plat_resto_evenement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='img',
            field=models.ImageField(upload_to='evenement/'),
        ),
    ]