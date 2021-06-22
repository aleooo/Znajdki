from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('objects/', views.RzeczyListView.as_view(), name='objects_list'),
    path('objects/<pk>/', views.RzeczyDetailView.as_view(), name='objects_detail'),
]