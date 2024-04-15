from django.urls import path
from . import views



urlpatterns = [
    path('' , views.index),
    path('new', views.new, name='login'),
    path('view_logins', views.view_logins, name='leakage'),
    path('show_visits', views.show_visits, name='Num_of_visits'),
    
]