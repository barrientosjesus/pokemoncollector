from django.db import models
from django.urls import reverse


class Trainer(models.Model):
    name = models.CharField(max_length=30)
    badges = models.IntegerField("Badges Won")
    is_gym_leader = models.BooleanField("Gym Leader", default=False)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('details', kwargs={'trainer_id': self.id})


class Move(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, default="Normal")
    power_point = models.IntegerField("PP")
    power = models.IntegerField()
    accuracy = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('moves_detail', kwargs={'pk': self.id})


class Pokemon(models.Model):
    pokedex_number = models.IntegerField("Pokedex Number")
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, default='', blank=True, null=True)
    type = models.CharField("Pokemon Type", max_length=50, default='')

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    moves = models.ManyToManyField(Move)

    def __str__(self):
        return f"{self.name} #{self.pokedex_number}"

    def get_absolute_url(self):
        return reverse('details', kwargs={'pokemon_id': self.id})
