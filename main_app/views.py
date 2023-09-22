from django.shortcuts import render

pokemon = [
    {'id': '0001', 'name': 'Bulbasaur', 'types': ['Grass', 'Poison']},
    {'id': '0002', 'name': 'Ivysaur', 'types': ['Grass', 'Poison']},
    {'id': '0008', 'name': 'Wartortle', 'types': ['Water']}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    return render(request, 'pokemon/pokemon_index.html', {
        'pokemon': pokemon,
    })