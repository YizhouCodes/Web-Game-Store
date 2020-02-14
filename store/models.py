from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class GeneralUser(AbstractUser):

    # DO NOT CHANGE the order
    PLAYER = 1
    DEVELOPER = 2
    USER_TYPE_CHOICES = (
        (PLAYER, 'Player'),
        (DEVELOPER, 'Developer'),
    )

    date_of_birth = models.DateField(default="2020-02-20")
    payment_info = models.TextField(default="")

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=PLAYER)

    REQUIRED_FIELDS = ['payment_info', 'date_of_birth', 'email']

    def is_player(self):
        return self.user_type == GeneralUser.PLAYER

    def is_developer(self):
        return self.user_type == GeneralUser.DEVELOPER

class Game(models.Model):
    title = models.CharField(max_length=256)
    developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    dateOfUpload = models.DateField()
    screenshots = models.URLField()
    averageRating = models.FloatField()
    category = models.CharField(max_length=32)
    price = models.FloatField()
    minimumAge = models.IntegerField()
    url = models.URLField()
    purchases = models.IntegerField(default=0)
    moneyEarned = models.FloatField(default=0.0)

class Review(models.Model):
    gameId = models.ForeignKey('Game', on_delete=models.CASCADE)
    playerId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()
    description = models.TextField()

class PlayersGames(models.Model):
    gameId = models.ForeignKey('Game', on_delete=models.CASCADE)
    playerId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.FloatField()
    gameState = models.TextField()
