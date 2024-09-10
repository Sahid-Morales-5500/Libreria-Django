from django.urls import path
from Aplicaciones import views

urlpatterns = [
    path('', views.Index)
]