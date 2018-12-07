from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView
from .models import Trabajo
from Trabajos.forms import CreateForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def bolsa(request):
    trabajos = Trabajo.objects.all()
    return render( request, "trabajos/bolsa-de-trabajo.html", { 'trabajos': trabajos})

#class PostListView(ListView):
#    model = Trabajo
#    template_name = 'trabajos/bolsa-de-trabajo.html'
#    context_object_name = 'Trabajos'