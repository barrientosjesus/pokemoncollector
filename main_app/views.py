from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trainer
from .forms import PokemonForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def trainer_index(request):
    trainer = Trainer.objects.all()
    return render(request, 'trainer/index.html', {
        'trainer': trainer,
    })

def trainer_details(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    pokemon_form = PokemonForm()
    return render(request, 'trainer/details.html', {
        'trainer': trainer,
        'pokemon_form': pokemon_form
    })

def add_pokemon(request, trainer_id):
    form = PokemonForm(request.POST)
    print(form.is_valid());
    if form.is_valid():
        new_pokemon = form.save(commit=False)
        new_pokemon.trainer_id = trainer_id
        new_pokemon.save()
    return redirect('details', trainer_id=trainer_id)

class TrainerCreate(CreateView):
    model = Trainer
    fields = '__all__'

class TrainerUpdate(UpdateView):
    model = Trainer
    fields = '__all__'

class TrainerDelete(DeleteView):
    model = Trainer
    success_url = '/trainer'