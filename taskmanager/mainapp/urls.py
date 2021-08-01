from django.urls import path, include
from . import views

urlpatterns = [
    path('taskmanager/', views.taskmanager, name='taskmanager'),
    path('update_task/<str:pk>/', views.update_task, name="update_task"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
]