from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('add',views.add, name='add'),
    path('addpost',views.addpost, name='addpost'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('update/<int:id>',views.update, name='update'),
    path('update/up/<int:id>',views.up, name='up'),
]