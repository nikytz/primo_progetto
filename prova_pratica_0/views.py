from django.shortcuts import render
import random
# Create your views here.
def maxmin(request):
    var1=random.randint(1,10)
    var2=random.randint(1,10)
    somma= var1 + var2
    context={
       'var1': var1,
       'var2': var2,
       'somma': somma,
    }
    return render (request,"prova_pratica_0/maxmin.html",context)

def media(request):
    somma=0
    for i in range (30):
        somma+=i 
    media= somma/30
    
    context={
        'media': media
    }
    return render (request,"prova_pratica_0/media.html",context)

def index(request):
    return render(request,"prova_pratica_0/index.html")