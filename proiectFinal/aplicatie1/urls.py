from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from aplicatie1 import views
from aplicatie1.views import MovieDetail

app_name = 'movieApplication'

urlpatterns = [
    path('', views.MoviesView.as_view(), name='lista_filme'),
    path('addMovie/', views.CreateMoviesView.as_view(), name='addMovie'),
    path('topRatedMovie/', views.MoviesTopRated.as_view(), name='topRatedMovie'),
    path('mostWatchedMovie/', views.MoviesMostWatched.as_view(), name='mostWatchedMovie'),
    path('recentlyAddedMovie/', views.MoviesRecentlyAdded.as_view(), name='recentlyAddedMovie'),
    path('<int:pk>/updateMovie/', views.UpdateMoviesView.as_view(), name='updateMovie'),
    path('<int:pk>/deleteMovie/', views.delete_movies, name='deleteMovie'),
    path('<int:pk>/activateMovie/', views.activate_movies, name='activateMovie'),
    path('inactiveMovies', views.MoviesInactiveView.as_view(), name='inactiveMovies'),
    path('searchMovies/', views.search_movies, name='searchMovies'),
    path('<int:pk>/movieDetails/', views.MovieDetail.as_view(), name='movieDetails'),
    path('register/', views.registerPage, name='register'),

    path('action/', views.MoviesAction.as_view(), name='action'),
    path('drama/', views.MoviesDrama.as_view(), name='drama'),
    path('comedy/', views.MoviesComedy.as_view(), name='comedy'),
    path('romance/', views.MoviesRomance.as_view(), name='romance'),
    path('adventure/', views.MoviesAdventure.as_view(), name='adventure'),
    path('love/', views.MoviesLove.as_view(), name='love'),
    path('cartoons/', views.MoviesCartoons.as_view(), name='cartoons'),


    # path('topRatedMovies', views.MoviesTopRated.as_view(), name='topRatedMovies'),
    # path('mostWatchedMovies', views.MoviesMostWatched.as_view(), name='mostWatchedMovies'),
    # path('recentlyAddedMovies', views.MoviesRecentlyAdded.as_view(), name='recentlyAddedMovies'),


]