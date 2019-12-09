from django.shortcuts import render, redirect
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
# Formularios
from .forms import FormRegUsuario, FormEditUsuario
# Autenticación de Usuario
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Custom Decorators
from main.decorators import admin_required
# Modelo User
from django.contrib.auth.models import User as UserModel

# Registro de Usuario
def UserRegView(request):
    # Si el usuario ya está autenticado redirecciona a Homepage
    if request.user.is_authenticated:
        return redirect('main:index')
    
    if request.method == 'POST':
        formulario = FormRegUsuario(request.POST)

        if formulario.is_valid():
            # Se guarda al usuario con los datos del formulario
            user = formulario.save()

            # Modelo Profile es creado despues de llamar a save()
            # por esto se actualiza la BD para cargar el Profile de user
            user.refresh_from_db()

            # Se redefinen los valores del perfil del usuario
            user.profile.nombre = formulario.cleaned_data.get('nombre')
            user.profile.fecnac = formulario.cleaned_data.get('fecnac')
            user.profile.fono =  formulario.cleaned_data.get('fono')
            user.profile.direccion = formulario.cleaned_data.get('direccion')
            user.profile.region = formulario.cleaned_data.get('region')
            user.profile.comuna = formulario.cleaned_data.get('comuna')
            user.profile.es_usuario = True
            
            # Se guarda al user y con este el perfil
            user.save()

            #  Deja al usuario logueado automaticamente
            raw_password = formulario.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            
            # Si nada salio mal, redirige a main/registrado.html
            return redirect('usuarios:reg_exitoso')

    else:
        formulario = FormRegUsuario()
    
    # Define el formulario en el contexto
    context = { 'form_reg': formulario, }

    return render(request, 'usuarios/registro.html', context=context)

# Registro Exitoso
def UserRegExitosoView(request):
    return render(request, 'usuarios/reg_exitoso.html')

# Listado de Usuarios
@login_required
@admin_required
def LstUsuariosView(request):
    # no_users: Error, si no se encontro ningun usuario en la BD
    context = {
        'no_users' : False,
        'lst_users':'',
    }

    try:
        # Se consulta una lista con todos los usuarios y se guarda en el contexto
        context['lst_users']  =  UserModel.objects.all()
        
    except ObjectDoesNotExist:
        # Si no se encuentra ninguno se define el error
        context['no_users'] = True

    return render(request, 'usuarios/lst_usuarios.html', context=context)

# Perfil de Usuario
@login_required
def PerfilUsuarioView(request, pk, desde_lst):
    context = {
        'usuario':'',   # Usuario a editar
        'ORM':False,    # Error: No se encontro en la BD
        'meta':'',      # Diccionario con la información a mostrar en pantalla
        'desde_lst':desde_lst,  # Indica desde donde se entro
        'errors':'',    # Posibles errores
    }

    try:
        # del_error define si hubo un error al eliminar un usuario
        if request.session.__getitem__('del_error'):
            context['errors']='* Hubo un eror al momento de eliminar al usuario'
            request.session.__setitem__('del_error',False)
    except:
        pass

    try:
        # Se busca al usuario a mostrar
        u = UserModel.objects.get(pk = pk)
        context['usuario'] = u
        
        # Se define meta dependiendo del tipo de usuario
        # Admin muestra más datos que Cliente
        if(request.user.profile.es_admin):
            # tipo: Tipo de Usuario
            tipo = 'no_data'
            if u.profile.es_admin:
                tipo = 'Admin'
            elif u.profile.es_usuario:
                tipo = 'Usuario'

            meta = {
                'ID':u.id,
                'Nombre de Usuario':u.username,
                'Mail':u.email,
                'Nombre':u.profile.nombre,
                'Fecha de Nacimiento':u.profile.fecnac,
                'Teléfono':u.profile.fono,
                'Dirección':u.profile.direccion,
                'Región':u.profile.region,
                'Comuna':u.profile.comuna,
                'Tipo de Usuario':tipo
            }
        else:
            meta = {
                'Nombre de Usuario':u.username,
                'Mail':u.email,
                'Nombre':u.profile.nombre,
                'Fecha de Nacimiento':u.profile.fecnac,
                'Teléfono':u.profile.fono,
                'Dirección':u.profile.direccion,
                'Región':u.profile.region,
                'Comuna':u.profile.comuna,
            }
        
        context['meta']=meta

    except ObjectDoesNotExist:
        # Si no se encuentra al usuario se manda un error
        context['ORM'] = True

    return render(request, 'usuarios/perfil_usuario.html', context=context)

# Editar Usuario
@login_required
def EditarUsuarioView(request, pk, desde_lst):
    # Si el usuario no es admin, no puede editar un usuario con pk diferente
    if request.user.pk!=pk and not request.user.profile.es_admin:
        return redirect('/accounts/login/?next=%s' % request.path)

    context = {
        'usuario':'',   # Usuario a editar
        'ORM':False,    # Error: No se encontro en la BD
        'form_reg':'',  # Formulario a usar
        'reg':'',       # Región. Necesario por como funcionan las combobox
        'com':'',       # Comuna. Idem
        'desde_lst':desde_lst   # Indica desde donde se entro
    }

    try:
        # Consigue al usuario a editar y lo define en el contexto
        u = UserModel.objects.get(pk = pk)
        context['usuario'] = u

        # Diccionario con los datos iniciales para el formulario
        init_data = {
            'username': u.username, 
            'email': u.email, 
            'nombre': u.profile.nombre, 
            'fecnac': u.profile.fecnac, 
            'fono': u.profile.fono, 
            'direccion': u.profile.direccion,
            'region': u.profile.region,
            'comuna': u.profile.comuna,
        }
        context['region']=u.profile.region
        context['comuna']=u.profile.comuna

    except ObjectDoesNotExist:
        # Si no se encuentra al usuario en la BD se define el error
        context['ORM']=True
        render(request, 'usuarios/editar_usuario.html', context=context)

    # Si se solicita un POST
    if request.method == 'POST':
        # Consigue la instancia más actual del usuario a editar
        instance = UserModel.objects.get(pk = pk)
        # Carga el formulario con los datos iniciales e indicando que es POST
        formulario = FormEditUsuario(request.POST, instance=instance)

        # Si el formulario es valido
        if formulario.is_valid():
            # Se guarda al usuario con los datos del formulario
            user = formulario.save()

            # Modelo Profile es creado despues de llamar a save()
            # por esto se actualiza la BD para cargar el Profile de user
            user.refresh_from_db()

            # Se redefinen los valores del perfil del usuario
            user.profile.nombre = formulario.cleaned_data.get('nombre')
            user.profile.fecnac = formulario.cleaned_data.get('fecnac')
            user.profile.fono =  formulario.cleaned_data.get('fono')
            user.profile.direccion = formulario.cleaned_data.get('direccion')
            user.profile.region = formulario.cleaned_data.get('region')
            user.profile.comuna = formulario.cleaned_data.get('comuna')
            
            # Se guarda al user y con este el perfil
            user.save()

            # Si nada salio mal, redirecciona al perfil de usuario
            return redirect('/accounts/perfil/{}/{}'.format(pk, desde_lst))

    else:
        # Carga el formulario con los datos iniciales
        formulario = FormEditUsuario(initial=init_data)

    # Define el formilario en el contexto
    context['form_reg'] = formulario

    return render(request, 'usuarios/editar_usuario.html', context=context)

# Eliminar Usuario
@login_required
@admin_required
def EliminarUsuarioView(request, pk, desde_lst):
    
    try:
        d = UserModel.objects.get(pk = pk)
        
        d.delete()

        request.session.__setitem__('del_error',False)

        return redirect('usuarios:lst_usuarios')
        
    except:
        # Si hubo un error durante la eliminación se indica en del_error en al sesión
        request.session.__setitem__('del_error',True)
        
        return redirect('usuarios:perfil_usuario', pk, desde_lst)

    return redirect('usuarios:perfil_usuario', pk, desde_lst)



