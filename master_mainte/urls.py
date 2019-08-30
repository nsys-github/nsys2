from django.urls import path

from . import views

app_name = 'master_mainte'
urlpatterns = [
    path('', views.index, name='index'),
]
