from django.db import models
from django.urls import reverse


class Pokemon(models.Model):
    pokedexNumber = models.IntegerField()
    name = models.CharField(max_length=30)
    pokeType = models.CharField(max_length=50)
    types = models.JSONField()

    def __str__(self):
        return f"{self.name} #{self.pokedexNumber}"

    def get_absolute_url(self):
        return reverse('details', kwargs={'pokemon_id': self.id})
