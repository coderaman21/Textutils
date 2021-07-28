from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='todohome'),
    path('tasks', views.tasks, name='tasks'),
    path('tasks/<str:myid>/', views.taskdetail, name='taskdetail'),
    path('search', views.search, name='search'),

]