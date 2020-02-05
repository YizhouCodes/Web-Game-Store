from rest_framework import serializers
from store.models import Game, PlayersGames, GeneralUser

class GeneralUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneralUser
        fields = ['pk', 'username', 'email']

class GameSerializer(serializers.ModelSerializer):
    developer = GeneralUserSerializer(many=False, read_only=True)

    def __init__(self, *args, **kwargs):
        super(serializers.ModelSerializer, self).__init__(*args, **kwargs)
        print("__init__ called")
        if 'context' in kwargs:
            if 'request' in kwargs['context']:
                excluding = kwargs['context']['request'].query_params.getlist('excluding', [])
                if excluding:
                    if ',' in excluding[0]:
                        excluding = excluding[0].split(',')

                    excluding = set(excluding)
                    for f in excluding:
                        self.fields.pop(f)

    class Meta:
        model = Game
        fields = ['title', 'developer', 'description', 'dateOfUpload', 'averageRating', 'category', 'price', 'minimumAge', 'purchases']

class HighscoreSerializer(serializers.ModelSerializer):
    gameId = serializers.SlugRelatedField(many=False, read_only=True, slug_field='pk')
    class Meta:
        model = PlayersGames
        fields = ['gameId', 'score']