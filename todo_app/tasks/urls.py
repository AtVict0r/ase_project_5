from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('completed', views.completed, name='completed'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('detail', views.detail, name='detail'),
    path('remaining', views.remaining, name='remaining'),
    path('edit', views.edit, name='edit'),
]