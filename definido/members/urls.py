from django.urls import path 
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
     path('name/<str:name>', views.name, name = 'name'),
     path('' , views.members),
     path('exercise/',views.exercise),
]