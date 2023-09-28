from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Trainer, Move, Pokemon
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
        'pokemon_form': pokemon_form,
    })


def assoc_pokemon(request, move_id):
    pokemon_id = str(request.POST['pokemon_id'])
    Pokemon.objects.get(id=pokemon_id).moves.add(move_id)
    return redirect('moves_detail', move_id=move_id)


def remove_pokemon(request, move_id, pokemon_id):
    Pokemon.objects.get(id=pokemon_id).moves.remove(move_id)
    return redirect('moves_detail', move_id)


def add_pokemon(request, trainer_id):
    form = PokemonForm(request.POST)
    if form.is_valid():
        new_pokemon = form.save(commit=False)
        new_pokemon.trainer_id = trainer_id
        new_pokemon.save()
    return redirect('details', trainer_id=trainer_id)


def move_details(request, move_id):
    move = Move.objects.get(id=move_id)
    pokemon_list = Pokemon.objects.all()
    return render(request, 'main_app/move_detail.html', {
        'move': move,
        'pokemon_list': pokemon_list
    })


class TrainerCreate(CreateView):
    model = Trainer
    fields = '__all__'


class TrainerUpdate(UpdateView):
    model = Trainer
    fields = '__all__'


class TrainerDelete(DeleteView):
    model = Trainer
    success_url = '/trainer'


class MoveList(ListView):
    model = Move


class MoveCreate(CreateView):
    model = Move
    fields = '__all__'


class MoveUpdate(UpdateView):
    model = Move
    fields = '__all__'


class MoveDelete(DeleteView):
    model = Move
    success_url = '/moves'
