from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trainer/', views.trainer_index, name='index'),
    path('trainer/<int:trainer_id>/', views.trainer_details, name='details'),
    path('trainer/create/', views.TrainerCreate.as_view(), name='trainer_create'),
    path('trainer/<int:pk>/update/', views.TrainerUpdate.as_view(), name='trainer_update'),
    path('trainer/<int:pk>/delete/', views.TrainerDelete.as_view(), name='trainer_delete'),
    path('trainer/<int:trainer_id>/add_pokemon/', views.add_pokemon, name='add_pokemon'),
    path('moves/', views.MoveList.as_view(), name='moves_index'),
    path('moves/<int:move_id>/', views.move_details, name='moves_detail'),
    path('moves/create/', views.MoveCreate.as_view(), name='moves_create'),
    path('moves/<int:pk>/update/', views.MoveUpdate.as_view(), name='moves_update'),
    path('moves/<int:pk>/delete/', views.MoveDelete.as_view(), name='moves_delete'),
    path('moves/<int:move_id>/assoc_pokemon/', views.assoc_pokemon, name='assoc_pokemon'),
    path('moves/<int:move_id>/remove_pokemon/<int:pokemon_id>/', views.remove_pokemon, name='remove_pokemon'),
]
