from django.urls import path
from movies import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('recommendations/', views.recommendations, name='recommendations'),
]