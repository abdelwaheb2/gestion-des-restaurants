# Generated by Django 4.1.5 on 2023-01-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resto',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='resto',
            name='etoiles',
            field=models.IntegerField(default=0),
        ),
    ]