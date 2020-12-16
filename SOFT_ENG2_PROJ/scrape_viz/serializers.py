from rest_framework import serializers
from scrape_viz.models import Movie, Weather

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title','year','ratings','metascore','votes','gross_income']


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id','night_period','day_period','night_temp','day_temp','night_humidity','day_humidity']