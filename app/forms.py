from django import forms
from .models import Contacto,Cita
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class CitaForm(forms.ModelForm):  

    fecha_consulta = forms.DateField(widget=forms.SelectDateWidget(attrs={"class":"form-control"}))

    class Meta:
        model = Cita
        fields = '__all__'