# App
Proyecto de prueba para postulación a práctica en Lab4U

# Especificaciones
- Webapp en [Django](https://www.djangoproject.com/)
- [django-widget-tweaks 1.4.5](https://pypi.org/project/django-widget-tweaks/) **(Necesario instalar para correr el proyecto)** 
- [Bootstrap 4.3.1](https://getbootstrap.com/)
- [Popper.js](https://popper.js.org/)
- [JQuery 3.4.1](https://jquery.com/)
- [Material Icons](https://google.github.io/material-design-icons/)

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
