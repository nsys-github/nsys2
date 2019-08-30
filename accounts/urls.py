from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('', views.signup, name='signup'),
    # ex: /contract/5/quotation/
]
