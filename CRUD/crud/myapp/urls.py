from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Page d'accueil avec la liste des membres
    path('add/', views.add, name='add_member'),  # Affichage et soumission du formulaire d'ajout
    path('delete/<int:id>/', views.delete, name='delete_member'),  # Suppression d'un membre
    path('update/<int:id>/', views.update_member, name='update_member'),  # Affichage et soumission du formulaire de mise à jour
]