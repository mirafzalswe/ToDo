from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo-index'),
    path('about/', views.about, name="todo-about"),
    path('login/', views.login, name='todo-login'),
    path('register/', views.register, name='todo-register'),
    path('todo/', views.todo, name='todo-project')
]
