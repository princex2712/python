from django.urls import path
from .views import *

urlpatterns = [
    path('',booksListAPI,name="booksListAPI" ),
    path('book/<int:id>',bookDetailAPI,name="bookDetailAPI"),
]
