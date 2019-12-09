from django import forms

from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User

# Formulario de registro de Usuarios
class FormRegUsuario(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','password1', 'password2', 'nombre', 'fecnac', 'email', 'fono', 
                'direccion', 'region', 'comuna')

    username = UsernameField( label='Nombre de Usuario', required=True,
        widget=forms.TextInput(attrs={ 'autofocus': True, 'type':'text', }) )

    password1 = forms.CharField( label='Contraseña', required=True, 
        widget=forms.PasswordInput(attrs={ 'type':"password" }) )

    password2 = forms.CharField( label='Confirmar Contraseña', required=True, 
        widget=forms.PasswordInput(attrs={ 'type':"password" }) )

    email = forms.EmailField( label='Email', required=True, 
        widget=forms.TextInput(attrs={'type':"email",}) )

    
    nombre = forms.CharField( label='Nombre Completo', required=True,
        widget=forms.TextInput(attrs={ 'type':'text', }) )

    
    fecnac = forms.CharField( label='Fecha de Nacimiento', required=True,
        widget=forms.TextInput(attrs={ 'type':'date', }) )

    
    fono = forms.IntegerField( label='Teléfono de contacto', required=True,
        min_value=100000000, max_value=999999999)
    
    direccion = forms.CharField( label='Dirección', required=True,
        widget=forms.TextInput(attrs={ 'type':'text', }) )
    
    region = forms.CharField( label='Región', 
        widget=forms.Select(attrs={ 'id':'regiones' }) )

    comuna = forms.CharField( label='Comuna',
        widget=forms.Select(attrs={ 'id':'comunas' }) )

# Formulario de Edición de Usuario
class FormEditUsuario(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'nombre', 'fecnac', 'email', 'fono', 
                'direccion', 'region', 'comuna')

    username = UsernameField( label='Nombre de Usuario', required=True,
        widget=forms.TextInput(attrs={ 'autofocus': True, 'type':'text', }) )

    email = forms.EmailField( label='Email', required=True, 
        widget=forms.TextInput(attrs={'type':"email",}) )

    
    nombre = forms.CharField( label='Nombre Completo', required=True,
        widget=forms.TextInput(attrs={ 'type':'text', }) )

    
    fecnac = forms.CharField( label='Fecha de Nacimiento', required=True,
        widget=forms.TextInput(attrs={ 'type':'date' }) )

    
    fono = forms.IntegerField( label='Teléfono de contacto', required=True,
        min_value=100000000, max_value=999999999)
    
    direccion = forms.CharField( label='Dirección', required=True,
        widget=forms.TextInput(attrs={ 'type':'text', }) )
    
    region = forms.CharField( label='Región', 
        widget=forms.Select(attrs={ 'id':'regiones' }) )

    comuna = forms.CharField( label='Comuna',
        widget=forms.Select(attrs={ 'id':'comunas' }) )

