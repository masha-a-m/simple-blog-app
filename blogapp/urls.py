from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),

    # path('readmore/<str:slug>', views.readmore, name = 'readmore'),
    path('blogapp/<str:slug>', views.readmore, name = 'readmore')
]