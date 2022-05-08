from django.urls import path

from aplicatie1 import views

app_name = 'locations'

urlpatterns = [
    path('', views.LocationView.as_view(), name='lista_locatii'),
    path('add/', views.CreateLocationView.as_view(), name='add'),
    path('<int:pk>/update/', views.UpdateLocationView.as_view(), name='modifica'),
    path('<int:pk>/delete/', views.delete_location, name='sterge'),
    path('<int:pk>/activeaza/', views.activate_location, name='activeaza'),
    path('locatii_inactive', views.LocationInactiveView.as_view(), name='locatii_inactive')
]