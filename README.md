# App
Proyecto de prueba para postulación a práctica en Lab4U

# Especificaciones
- Webapp en [Django](https://www.djangoproject.com/)
- [django-widget-tweaks 1.4.5](https://pypi.org/project/django-widget-tweaks/) **(Necesario instalar para correr el proyecto)** 
- [Bootstrap 4.3.1](https://getbootstrap.com/)
- [Popper.js](https://popper.js.org/)
- [JQuery 3.4.1](https://jquery.com/)
- [Material Icons](https://google.github.io/material-design-icons/)
- Base de Datos en SQLite

# Funcionalidades
- Registro y Login de Usuario
- Modelo de User con sistema de autenticación por Django
- La información adicional del Usuario se guarda en la tabla Profile con relación 1..1 a User
- Tipos de Usuario: Admin y Cliente
- Consulta de Perfil de Usuario
- Edición de Perfil de Usuario
- Formulario de Registro y Edición de Usuario con validación de datos
- Administración de Usuarios por Admin
- Restricción de acceso a páginas dependiendo del Tipo de Usuario
  - Anonimo: 
    - Registro y Login
  - Cliente: 
    - Perfil personal
  - Admin: 
    - Perfil Personal
    - Lista de Usuarios
    - Perfil de Otros Usuarios
    - Editar Otros Usuarios
    - Eliminar Otros Usuarios

# Usuarios Predefinidos
- Usuario Admin
  - admin  |  admin
- Usuario Cliente
  - Cliente   |  alfalfa8
  - Cliente2  |  alfalfa8
  
# Patron de Arquitectura - MTV
Django por defecto usa una arquitectura MTV (Model Template View), que es similar en funcionamiento a una arquitectura MVC (Model View Controller), pero en Django se tiene
- Model : Modelo, al igual que en MVC, representa los datos en la base de datos y sirve se interface a los datos en duro. Además, permite interactuar con los datos usando el ORM por defecto de Django que trabaja con una BD local en SQLite.
- Template : Similar a la vista en MVC, es la capa de presentación que el usuario final ve. Django usa un sistema de tags y variables que son evaluados al momento de cargar la pagina y definen la lógica de presentación.
- View : Paralelo a lo que sería el controlador en MCV, maneja la lógica de negocios y define un contexto en el que se basará el Template cuando se redireccione a este.
De esta manera se puede decir que, a grandes razgos, el Model define la estructura de datos del proyecto, la View se encarga de la lógica de negocios de cada petición y el Template se encarga de tomar el contexto dado por la View y ordenarlo de manera adecuada para el usuario final.
