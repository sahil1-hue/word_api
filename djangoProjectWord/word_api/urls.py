from django.urls import path
from .import views
urlpatterns = [
    path('',  views.word_api, name =' word_search')


]