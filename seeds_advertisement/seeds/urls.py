from django.urls import path

from . import views

app_name = 'seeds_advertisement'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('advertisements/<int:advertisement_id>/', views.advertisements_detail_view, name='advertisements_detail'),
    path('advertisements/', views.advertisements_view, name='advertisements'),
    path('farmers/', views.farmers_view, name='farmers'),
]