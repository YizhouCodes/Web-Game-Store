from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from store.models import Game, PlayersGames, GeneralUser
from store_rest_api_v1.serializers import GameSerializer, HighscoreSerializer, GeneralUserSerializer

class UsersView(viewsets.ModelViewSet):
    queryset = GeneralUser.objects.all()
    serialization_class = GeneralUserSerializer

class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'category', 'description', 'developer__username']
    filterset_fields = ['averageRating', 'dateOfUpload', 'price', 'minimumAge', 'purchases']
    ordering_fields = ['title', 'category', 'averageRating', 'dateOfUpload', 'price', 'minimumAge', 'purchases']
    ordering = ['purchases']

class HighscoreListView(generics.ListAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PlayersGames.objects.all()
    serializer_class = HighscoreSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['gameId']
    ordering_fields = ['score']
    ordering = ['score']
