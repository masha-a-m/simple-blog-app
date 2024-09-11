from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('blogapp/<str:slug>', views.readmore, name = 'readmore')
]