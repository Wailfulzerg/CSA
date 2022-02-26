from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .models import Cinema, Hall, Event
from .serializers import CinemaSerializer, HallSerializer, EventSerializer, CreateEventSerializer
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend


class CinemaViewSet(ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['name', 'address', 'afisha_id', 'url']

    @action(["GET"], detail=True)
    def available_dates(self, request, pk=None):
        cinema = self.get_object()
        return Response(status=status.HTTP_200_OK, data={'dates': cinema.available_dates})



class HallViewSet(ModelViewSet):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    filterset_fields = ['name', "cinema"]


class EventViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateEventSerializer
        return EventSerializer
    queryset = Event.objects.all()
    filterset_fields = ["cinema", "hall", "movie", "date", "time"]

