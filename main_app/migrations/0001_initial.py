# Generated by Django 4.2.5 on 2023-09-25 18:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokedexNumber', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('name', models.CharField(max_length=30)),
                ('pokeType', models.CharField(max_length=50)),
                ('types', models.JSONField()),
            ],
        ),
    ]
