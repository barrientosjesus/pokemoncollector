from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Pokemon(models.Model):
    pokedexNumber = models.IntegerField(validators=[MinValueValidator(1)])
    name = models.CharField(max_length=30)
    pokeType = models.CharField(max_length=50)
    types = models.JSONField()

    def __str__(self):
        return f"{self.name} #{self.pokedexNumber}"