from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Los usuarios usan el modelo por defecto User de Django
# Para más información se usa otra tabla Profile con relacion 1..1 con auth.models.User
class Profile(models.Model):
    # auth.models.User asociado
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Datos del Usuario
    nombre = models.CharField(max_length = 100)
    fecnac = models.DateField(default=timezone.now)
    fono = models.CharField(max_length = 50)
    direccion = models.CharField(max_length=100)
    region = models.CharField(max_length = 100)
    comuna = models.CharField(max_length = 100)
    
    # Tipo de Usuario
    es_admin = models.BooleanField(default=False)
    es_usuario = models.BooleanField(default=False)
    
    def __str__(self):
       return self.user.username


# Signal que crea una instancia o actualiza Profile cada vez que un User cambia
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
