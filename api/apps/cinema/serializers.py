from rest_framework import serializers
from .models import Cinema, Hall, Event
from movies.serializers import MovieSerializer


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'

class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer()
    movie = MovieSerializer()
    hall = HallSerializer()

    class Meta:
        model = Event
        fields = '__all__'
