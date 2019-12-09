from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='usuarios:login'):
    '''
    Decorator para Views que ve si el usuario activo es Admin y redirige
    a la página de Login si no lo es
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.profile.es_admin,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

