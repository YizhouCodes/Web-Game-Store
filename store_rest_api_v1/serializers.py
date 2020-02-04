from rest_framework import serializers
from store.models import Game, PlayersGames, GeneralUser

class GeneralUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneralUser
        fields = ['pk', 'username', 'email']

class GameSerializer(serializers.HyperlinkedModelSerializer):
    developer = GeneralUserSerializer(many=False, read_only=True)
    class Meta:
        model = Game
        fields = ['title', 'developer', 'description', 'dateOfUpload', 'averageRating', 'category', 'price', 'minimumAge', 'purchases']


class HighscoreSerializer(serializers.HyperlinkedModelSerializer):
    gameId = serializers.SlugRelatedField(many=False, read_only=True, slug_field='pk')
    class Meta:
        model = PlayersGames
        fields = ['gameId', 'score']