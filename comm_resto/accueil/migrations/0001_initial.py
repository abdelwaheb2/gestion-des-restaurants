# Generated by Django 4.1.5 on 2023-01-27 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='photos/pub')),
                ('des', models.TextField()),
                ('date', models.DateField()),
                ('dure', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
