from django.urls import path
from . import views

app_name = 'rest_framework'

urlpatterns = [
    path('', views.api_overview, name='overview'),
    path('finds/', views.finds_list_view, name='finds_list'),
    path('finds/<int:pk>/', views.FindsUpdateView.as_view(), name='finds_detail'),
]