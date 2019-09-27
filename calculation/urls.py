from django.urls import path
from . import views

urlpatterns = [
    path('', views.calc_op, name='calc_op'),
]