from django.contrib import admin
from .models import Pokemon, Trainer

# Register your models here.
admin.site.register(Trainer)
admin.site.register(Pokemon)