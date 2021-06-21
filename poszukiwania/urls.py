from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from . import views


app_name = 'poszukiwania'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('add/', views.create, name='create'),
    path('catalog/', views.objects_list, name='objects_list'),
    path('search/', views.search, name='search'),
    path('', views.start, name='start'),
    path('update/<int:id>/', views.update, name='update'),
    path('<slug:category_slug>/', views.objects_list, name='objects_list_by_category'),
    path('<int:year>/<int:month>/<int:day>/<slug:object_slug>/<int:id>/', views.object_detail, name='object_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL)
