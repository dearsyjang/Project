from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'
    

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'