from django.contrib import admin
from .models import Pokemon, Trainer, Move

# Register your models here.
admin.site.register(Trainer)
admin.site.register(Pokemon)
admin.site.register(Move)
