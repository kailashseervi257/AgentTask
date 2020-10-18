from django.urls import path
from .views import display, map

urlpatterns = [
    path('', display, name='Agent'),
    path('<str:lat>/<str:long>',map, name='map'),
]