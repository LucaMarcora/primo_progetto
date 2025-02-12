from django.shortcuts import render, get_object_or_404
from .models import Corso
import datetime

def index_corsi(request): #view index root
    return render(request, "index_corsi.html")

def view_a(request): #view di view a
    corsi = Corso.objects.order_by('data_inizio')
    context = {'corsi' : corsi}
    return render(request, 'view_a.html',context)

def view_b(request, pk): #view di view b
    corso = get_object_or_404(Corso, pk=pk)
    context = {"corso": corso}
    return render(request, "view_b.html", context)


def view_c(request): #view di view c
    corsi_data = Corso.objects.filter(data_inizio__gt=datetime.date(2025,5,1))
    context = {'corsi' : corsi_data}
    return render(request, 'view_c.html',context)   

def view_d(request): #view di view d
    corsi_meno_20 = Corso.objects.filter(posti_disponibili__lt=20)
    context = {'corsi' : corsi_meno_20}
    return render(request, 'view_d.html',context)  

def view_e(request): #view di view e
    corsi_data_fine = Corso.objects.filter(data_fine__lte=datetime.date(2025,4,30))
    context = {'corsi' : corsi_data_fine}
    return render(request, 'view_e.html',context)   


def view_f(request): #view di view f
    pass
    
