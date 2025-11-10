from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"prima_app/homepage.html")

def welcome(request):
    return render(request,"prima_app/welcome.html")

def lista(request):
    return render(request,"prima_app/lista.html")

def chi_siamo(request):
    return render(request,"prima_app/chi_siamo.html")

def variabili(request):
    context={
        'var1': 'prima variabile',
        'var2': 'seconda variabile',
        'var3': 'terza variabile'
    }
    return render(request,"prima_app/variabili.html",context)

def index(request):
    return render(request,"prima_app/index.html")