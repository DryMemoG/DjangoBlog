from django.urls import path
from . import views

urlpatterns = [
	path('',views.publicaciones, name='publicaciones'),
]