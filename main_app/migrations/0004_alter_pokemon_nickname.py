# Generated by Django 4.2.5 on 2023-09-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_poke_type_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='nickname',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]