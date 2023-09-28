from django.forms import ModelForm
from .models import Pokemon


class PokemonForm(ModelForm):
    class Meta:
        model = Pokemon
        fields = ['pokedex_number', 'name', 'nickname', 'type']
