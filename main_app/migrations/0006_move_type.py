# Generated by Django 4.2.5 on 2023-09-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_move_pokemon_moves'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='type',
            field=models.CharField(default='Normal', max_length=50),
        ),
    ]
