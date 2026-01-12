from django.urls import path
from .views import index, home, articoloDetailView

app_name='news'
urlpatterns = [
    path('',index,name='index'),
    path('home',home,name="homepage"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
]
