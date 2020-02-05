from rest_framework import viewsets, filters, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from store.models import Game, PlayersGames, GeneralUser
from store_rest_api_v1.serializers import GameSerializer, HighscoreSerializer, GeneralUserSerializer
from store_rest_api_v1.permissions import IsDeveloper

class UsersView(viewsets.ModelViewSet):
    queryset = GeneralUser.objects.all()
    serialization_class = GeneralUserSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated, IsDeveloper]

class GameListView(generics.ListAPIView):
    serializer_class = GameSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'category', 'description', 'developer__username']
    filterset_fields = ['averageRating', 'dateOfUpload', 'price', 'minimumAge', 'purchases']
    ordering_fields = ['title', 'category', 'averageRating', 'dateOfUpload', 'price', 'minimumAge', 'purchases']
    ordering = ['purchases']
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated, IsDeveloper]

    def get_queryset(self):
        queryset = Game.objects.all()

        min_avg_rating = self.request.query_params.get('min_averageRating', None)
        max_avg_rating = self.request.query_params.get('max_averageRating', None)

        min_date_of_upload = self.request.query_params.get('min_dateOfUpload', None)
        max_date_of_upload = self.request.query_params.get('max_dateOfUpload', None)

        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)

        min_minimumAge = self.request.query_params.get('min_minimumAge', None)
        max_minimumAge = self.request.query_params.get('max_minimumAge', None)

        min_purchases = self.request.query_params.get('min_purchases', None)
        max_purchases = self.request.query_params.get('max_purchases', None)

        if min_avg_rating:
            queryset = queryset.filter(avgRating__gte=min_avg_rating)
        if max_avg_rating:
            queryset = queryset.filter(avgRating__lte=max_avg_rating)
        if min_date_of_upload:
            queryset = queryset.filter(dateOfUpload__gte=min_date_of_upload)
        if max_date_of_upload:
            queryset = queryset.filter(dateOfUpload__lte=max_date_of_upload)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if min_minimumAge:
            queryset = queryset.filter(minimumAge__gte=min_minimumAge)
        if max_minimumAge:
            queryset = queryset.filter(minimumAge__lte=max_minimumAge)
        if min_purchases:
            queryset = queryset.filter(purchases__gte=min_purchases)
        if max_purchases:
            queryset = queryset.filter(purchases__lte=max_purchases)

        return queryset

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
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated, IsDeveloper]