from django.urls import path
from User import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('galeria/', views.galeria, name= 'galeria'),
    path('blog/', views.blog, name= 'blog'),
]