from django.shortcuts import render, redirect
from .models import Diploma
from .forms import DiplomaForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_client_ip(req):
    x_forwarded_for = req.META.get('HTTP_x_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')
    return str(ip)

def diploma_search(request):
    if request.method == 'POST':
        code = request.POST['code']
        try:
            diploma = Diploma.objects.get(codiceId=code)        
        except Diploma.DoesNotExist:
            messages.error(request, 'Nessun titolo di studio trovato con questo codice, riprovare')
            pass
        else:
            return redirect('diploma_detail', pk= diploma.pk)

    return render(request, 'myProject/diploma_search.html')

def diploma_detail(request, pk):
    diploma = Diploma.objects.get(pk=pk)
    return render(request, 'myProject/diploma_detail.html', {'diploma': diploma})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        psw = request.POST['psw']

        user = authenticate(username= username, password= psw)

        if user is not None:
            login(request, user)
            return redirect('restricted_area')
        else:
            messages.error(request, 'Username e/o password non validi, riprovare')
            pass
        
    return render(request, 'myProject/signin.html')

def signout(request):
    username = request.user.username
    ip_address = get_client_ip(request)
    r.set(username, ip_address)
    logout(request)
    return redirect('diploma_search')

def restricted_area(request):
    username = request.user.username
    ip_address = get_client_ip(request)
    if request.method == 'POST':
        form = DiplomaForm(request.POST)
        if form.is_valid():
            diploma = form.save()
            diploma.registra()
            return redirect('diploma_detail', pk=diploma.pk)
        else:
            messages.warning(request, 'Dati non validi')
    else:
        form = DiplomaForm()
    if r.exists(username) and r.get(username) != bytes(ip_address, 'utf-8'):
            messages.warning(request, 'ATTENZIONE, utente autenticato con indirizzo ip diverso rispetto a quello usuale')

    return render(request, 'myProject/restricted_area.html', {'form': form}) 
