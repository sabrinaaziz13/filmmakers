from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('about/', views.About.as_view(), name="about"),
  path('directors/', views.DirectorList.as_view(), name="director_list"),
  path('directors/new/', views.DirectorCreate.as_view(), name="director_create"),
  path('directors/<int:pk>/', views.DirectorDetail.as_view(), name="director_detail"),
  path('directors/<int:pk>/update', views.DirectorUpdate.as_view(), name="director_update"),
  path('directors/<int:pk>/delete', views.DirectorDelete.as_view(), name="director_delete"),
  path('directors/<int:pk>/movies/new/', views.MovieCreate.as_view(), name="movie_create"),
  path('movies/', views.MovieList.as_view(), name="movie_list"),
  path('movies/<int:pk>/', views.MovieDetail.as_view(), name="movie_detail"),
  path('movies/<int:pk>/update', views.MovieUpdate.as_view(), name="movie_update"),
  path('movies/<int:pk>/delete', views.MovieDelete.as_view(), name="movie_delete"),
]