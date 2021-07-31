from django.urls import path
from . import views

urlpatterns = [
    path('taskmanager/', views.taskmanager, name='taskmanager'),
    path('update_task/<str:pk>/', views.update_task, name="update_task"),
    path('connexion/', views.connection, name='connection'),
    path('', views.index, name='index'),
]
