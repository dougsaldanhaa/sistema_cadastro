from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
]
