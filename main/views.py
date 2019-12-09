from django.shortcuts import render, redirect
from django.views import generic

# Index, base para el resto de Vistas
def IndexView(request):

    return render(request, 'main/homepage.html')
