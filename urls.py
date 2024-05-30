from django.urls import path
from . import views

urlpatterns = [
    path('adicionar', views.add_usuario, name='add_usuario'),
]