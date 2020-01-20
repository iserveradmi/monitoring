from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tools/', views.tools, name='tools'),
    path('monitor/', views.monitor, name='monitor'),
]