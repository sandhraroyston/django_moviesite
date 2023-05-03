from . import views
from django.urls import path

app_name = 'movieapp'   #for setting app namespace url
urlpatterns = [
    path('', views.home,name='home'),
    path('movie/<int:movieid>', views.detail,name='detail'),
    path('add/', views.add,name='add_detail'),
    path('update/<int:id>', views.update,name='update'),
    path('genre/<str:moviegenre>/', views.genre,name='genre'),

]