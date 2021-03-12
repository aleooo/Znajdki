from django.urls import path
from . import views


app_name = 'poszukiwania'

urlpatterns=[
    path('', views.rzeczy_list, name='rzeczy_list'),
    path('<slug:kategoria_slug>/', views.rzeczy_list, name='rzeczy_list_by_category'),
    path('<int:year>/<int:month>/<int:day>/<slug:rzecz_slug>/<int:id>', views.rzecz_detail, name='rzecz_detail')
]