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
]