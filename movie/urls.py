from django.urls import path
from . import views

urlpatterns = [
    # path('studios/',views.studio_list,name='studio-list'),
    # path('studios/<int:pk>/',views.studio_detail,name="studio-detail"),
    path('studios/',views.StudioListAV.as_view(),name='studio-list'),
    path('studios/<int:pk>/',views.StudioDetailAV.as_view(),name="studio-detail"),
    path('genres/',views.GenreListAV.as_view(),name='genre-list'),
    path('movies/',views.MovieListAV.as_view(),name='movie-list'),
    path('movies/<int:pk>/',views.MovieDetailAV.as_view(),name="movie-detail"),
    path('movies/<int:pk>/form-update/',views.UpdateMovieImageAV.as_view(),name="movie-update"),
    
]
