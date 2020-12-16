from django.urls import path, include
from scrape_viz import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-view'),
    path('visualization/', include([
        path('movies/', views.MoviesVisualizationView.as_view() , name="visualization-movies"),
        path('movies/', include([
            path('data/', views.MoviesData.as_view(), name='movies-data'),
            path('data/id=<int:pk>/', views.MoviesData.as_view(), name='movie-data-id'),
            path('data/year=<int:year>/', views.MoviesData.as_view(), name='movie-data-year'),
        ])),
        path('weather/',views.WeatherVisualizationView.as_view(), name="visualization-weather"),
        path('weather/', include([
            path('data/', views.WeatherData.as_view(), name='weather-data'),
            path('data/id=<int:pk>/', views.WeatherData.as_view(), name='weather-data-id'),
            path('data/period=<slug:period>/', views.WeatherData.as_view(), name='weather-data-period'),
        ])),
        path("ecommerce/", views.EcommerceVisualizationView.as_view(), name="visualization-ecommerce"),
    ])),
    
]