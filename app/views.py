from django.shortcuts import render, redirect, get_list_or_404
from django.contrib import messages
from .forms import ContactoForm, CustomUserCreationForm, CitaForm, Cita
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):  
    data = {
        'form': CitaForm()
    }
    
    if request.method == 'POST':
        formulario = CitaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Cita Enviada"
        else:
            data["form"] = formulario  
    return render(request, 'app/index.html', data)

def contact(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'app/contact.html', data)

def about(request):
    return render(request, 'app/about.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def listar_pacientes(request):
    pacientes = Cita.objects.all()

    data = {
        'pacientes': pacientes
    }
    return render(request, 'app/pacientes/listar.html',data)

def modificar_cita(request,id):
    cita = get_list_or_404(Cita, id=id)
    data = {
        'form' : CitaForm(instance=cita)
    }
    return render(request, 'app/pacientes/modificar.html',data)