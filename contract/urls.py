from django.urls import path

from . import views

app_name = 'contract'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.TQuotationListView.as_view(), name='index'),
    # ex: /contract/5/quotation/
    path('<int:t_quotation_id>/quotation/', views.quotation, name='quotation'),
    path('<int:t_quotation_id>/contract/', views.contract, name='contract'),
    path('<int:t_quotation_id>/dispatch/', views.dispatch, name='dispatche'),
]
