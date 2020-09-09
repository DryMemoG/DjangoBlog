from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion

# Create your views here.
def publicaciones(request):
	publicacion = Publicacion.objects.all()
	return render(request, 'blog/publicaciones.html',{'publicaciones':publicacion})
