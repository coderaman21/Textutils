from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='todohome'),
    path('search', views.search, name='search'),

]