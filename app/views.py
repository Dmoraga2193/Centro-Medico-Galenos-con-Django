from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.

def index(request):    
    return render(request, 'app/index.html')

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
