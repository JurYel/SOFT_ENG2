from rest_framework import serializers
from scrape_viz.models import Movie, Weather, EcommerceLazada, EcommerceShopee

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title','year','ratings','metascore','votes','gross_income']


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id','night_period','day_period','night_temp','day_temp','night_humidity','day_humidity']

class EcommerceLazadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceLazada
        fields = ['id','prod_name','price']

class EcommerceShopeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceShopee
        fields = ['id','prod_name','price']