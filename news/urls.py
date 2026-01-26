from django.urls import path
from .views import index, home, articoloDetailView, listaArticoli

app_name='news'
urlpatterns = [
    path('',index,name='index'),
    path('home',home,name="homepage"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli")
]



