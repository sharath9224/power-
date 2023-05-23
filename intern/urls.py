from django.urls import path
from . import views

urlpatterns = [
    path('power_consumption/', views.power_consumption, name='power_consumption'),
    path('',views.index,name='index'),
]
