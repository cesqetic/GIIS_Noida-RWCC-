from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('economic/', views.economic, name='economic'),
    path('mental/', views.mentalhealth, name='mental'), 
    path('team/', views.team, name='team'),
]
