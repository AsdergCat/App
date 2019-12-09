
from django.urls import include, path
# from django.contrib.auth.views import AuthenticationForm
from django.contrib.auth import views as auth_views

from . import views

app_name = 'usuarios'
urlpatterns = [
    # ex: accounts/login/
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    # ex: accounts/logout/
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # ex: accounts/registrarse/
    path('registrarse/', views.UserRegView, name='user_reg'),
    # ex: accounts/reg_exitoso/
    path('reg_exitoso/', views.UserRegExitosoView, name='reg_exitoso'),
    
    # ex: accounts/lst_usuarios/
    path('lst_usuarios/', views.LstUsuariosView, name='lst_usuarios'),

    # ex: accounts/perfil/5/1
    path('perfil/<int:pk>/<int:desde_lst>', views.PerfilUsuarioView, name='perfil_usuario'),

    # ex: accounts/editar/5/0
    path('editar/<int:pk>/<int:desde_lst>', views.EditarUsuarioView, name='editar_usuario'),

    # ex: accounts/eliminar/5/0
    path('eliminar/<int:pk>/<int:desde_lst>', views.EliminarUsuarioView, name='eliminar_usuario'),
]
