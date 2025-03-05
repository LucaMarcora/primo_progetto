from django.urls import path
from .views import home, articoloDetailView, listaArticoli, index_news

app_name = 'news'

urlpatterns = [
    path('',home,name='homeview'),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli", listaArticoli, name="lista_articoli" ),
    path("index_news", index_news, name="index_news" ),
]
