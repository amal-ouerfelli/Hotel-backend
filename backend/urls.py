from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.test),
    path('client/', views.client)
    ]