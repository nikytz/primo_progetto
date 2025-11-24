from django.urls import path
from prova_pratica_0.views import maxmin, media, index

app_name="prova_pratica_0"
urlpatterns=[
    path('maxmin',maxmin, name='maxmin'),
    path('media',media, name='media'),
    path('',index,name='index'),
]


