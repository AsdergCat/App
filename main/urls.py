from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    # ex: /
    path('', views.IndexView, name='index'),
]
