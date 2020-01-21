from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class GeneralUser(AbstractUser):
    # Username: get_username()
    # Email: get_email_field_name()

    # DO NOT CHANGE the order
    PLAYER = 1
    DEVELOPER = 2
    USER_TYPE_CHOICES = (
        (PLAYER, 'Player'),
        (DEVELOPER, 'Developer'),
    )

    date_of_birth = models.DateField()
    payment_info = models.TextField()

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=PLAYER)

    REQUIRED_FIELDS = ['payment_info', 'date_of_birth', 'email']

    def is_player():
        return user_type == PLAYER

    def is_developer():
        return user_type == DEVELOPER
    

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
