from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.NewsDetail.as_view(), name='new-details'),
    path('<int:pk>/update', views.NewsUptade.as_view(), name='new-update'),
    path('<int:pk>/delete/', views.NewsDelete.as_view(), name='new-delete'),
]
