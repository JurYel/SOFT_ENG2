from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from scrape_viz.models import Movie, Weather, EcommerceLazada, EcommerceShopee
from scrape_viz.serializers import MovieSerializer, WeatherSerializer, EcommerceLazadaSerializer, EcommerceShopeeSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import os

home_page = True
class HomeView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'scrape_viz/home.html', {"home_page": home_page})

class MoviesVisualizationView(View):
    def get(self,request, *args, **kwargs):
        home_page = False
        return render(request, 'scrape_viz/movies_visualization.html', {"home_page": home_page})

class WeatherVisualizationView(View):
    def get(self,request, *args, **kwargs):
        home_page = False
        return render(request, 'scrape_viz/weather_visualization.html', {"home_page": home_page})

class EcommerceVisualizationView(View):
    def get(self, request, *args, **kwargs):
        home_page = False
        return render(request, 'scrape_viz/ecommerce_visualization.html', {"home_page": home_page})

class MoviesData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self,request,pk=None, year=None, format=None):
        if pk is None and year is None:
            if request.method == 'GET':
                movies = Movie.objects.using('movies_db').all()
                serializer = MovieSerializer(movies,many=True)
                return Response(serializer.data)

        else:
            if pk is not None:
                try:
                    movie = Movie.objects.using('movies_db').get(pk=pk)
                except Movie.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                if request.method == 'GET':
                    serializer = MovieSerializer(movie)
                    return Response(serializer.data)

            elif year is not None:
                movies = Movie.objects.using('movies_db').filter(year=year)
                if movies.count() < 1:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                if request.method == 'GET':
                    serializer = MovieSerializer(movies, many=True)
                    return Response(serializer.data)

class WeatherData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, pk=None, period=None, format=None):
        if pk is None and period is None:
            if request.method == 'GET':
                weathers = Weather.objects.using('weather_db').all()
                serializer = WeatherSerializer(weathers, many=True)
                return Response(serializer.data)

        else:
            if pk is not None:
                try:
                    weather = Weather.objects.using('weather_db').get(pk=pk)
                except Weather.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                if request.method == 'GET':
                    serializer = WeatherSerializer(weather)
                    return Reponse(serializer.data)
                
            elif period is not None:
                if period == 'day':
                    period = 'day_period'    
                    weathers = Weather.objects.using('weather_db').filter(day_period=period)
                    if weathers.count() < 1:
                        return Response(status=status.HTTP_404_NOT_FOUND)

                    if request.method == 'GET':
                        serializer = WeatherSerializer(weathers, many=True)
                        return Response(serializer.data)
                
                elif period == 'night':
                    period = 'night_period'
                    weathers = Weather.objects.using('weather_db').filter(night_period=period)
                    if weathers.count() < 1:
                        return Response(status=status.HTTP_404_NOT_FOUND)
                    
                    if request.method == 'GET':
                        serializer = WeatherSerializer(weathers, many=True)
                        return Response(serializer.data)


class EcommerceLazadaData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, pk=None, format=None):
        if pk is None:
            if request.method == 'GET':
                products = EcommerceLazada.objects.using('ecommerce_db').all()
                serializer = EcommerceLazadaSerializer(products, many=True)
                return Response(serializer.data)

        else:
            try:
                product = EcommerceLazada.objects.using('ecommerce_db').get(pk=pk)
            except EcommerceLazada.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if request.method == 'GET':
                serializer = EcommerceLazadaSerializer(product)
                return Response(serializer.data)


class EcommerceShopeeData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, pk=None, format=None):
        if pk is None:
            if request.method == 'GET':
                products = EcommerceShopee.objects.using('ecommerce_db').all()
                serializer = EcommerceShopeeSerializer(products, many=True)
                return Response(serializer.data)

        else:
            try:
                product = EcommerceShopee.objects.using('ecommerce_db').get(pk=pk)
            except EcommerceShopee.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if request.method == 'GET':
                serializer = EcommerceLazadaSerializer(product)
                return Response(serializer.data)

# def scrape_weather(request):
#     scrapy_signal.send() # sender = ?
#     return render()
