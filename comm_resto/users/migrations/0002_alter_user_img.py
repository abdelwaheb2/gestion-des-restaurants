# Generated by Django 4.1.5 on 2023-02-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(upload_to='photos/users'),
        ),
    ]
