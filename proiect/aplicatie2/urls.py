from django.urls import path

from aplicatie2 import views

app_name = 'companies'

urlpatterns = [
    path('', views.CompanyView.as_view(), name='listare'),
    path('adaugare/', views.CreateCompanyView.as_view(), name='add'),
    path('<int:pk>/update/', views.UpdateCompanyView.as_view(), name='modify'),
    path('<int:pk>/delete/', views.delete_company, name='delete'),
    path('<int:pk>/activate/', views.activate_company, name='activate'),
    path('companies_inactive', views.CompanyInactiveView.as_view(), name='companies_inactive'),

]
