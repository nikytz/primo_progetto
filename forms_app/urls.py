from django.urls import path
from forms_app.views import contatto , index, lista_contatti, elimina_contatto, modifica_contatto

app_name="forms_app"

urlpatterns=[
    path('', index , name="index"),
    path('contatto', contatto , name="contatto"),
    path('lista_contatti', lista_contatti , name="lista_contatti"),
    path('elimina_contatto/<int:pk>', elimina_contatto , name="elimina_contatto"),
    path('modifica_contatto/<int:pk>', modifica_contatto , name="modifica_contatto"),
    

]