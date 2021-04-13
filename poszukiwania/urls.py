from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings

app_name = 'poszukiwania'

urlpatterns=[
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('map/', views.add_map, name='map_create'),
    path('add/', views.create, name='create'),
    path('katalog/', views.rzeczy_list, name='rzeczy_list'),
    path('', views.start, name='start'),
    path('<slug:kategoria_slug>/', views.rzeczy_list, name='rzeczy_list_by_category'),
    path('<int:year>/<int:month>/<int:day>/<slug:rzecz_slug>/<int:id>', views.rzecz_detail, name='rzecz_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL)