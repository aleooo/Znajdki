from django.urls import path, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from . import views


app_name = 'poszukiwania'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('poszukiwania:password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('poszukiwania:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('poszukiwania:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('add/', views.create, name='create'),
    path('', views.objects_list, name='objects_list'),
    path('search/', views.search, name='search'),
    path('delete/<int:id>/', views.delete_objects, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('<slug:category_slug>/', views.objects_list, name='objects_list_by_category'),
    path('<int:year>/<int:month>/<int:day>/<slug:object_slug>/<int:id>/', views.object_detail, name='object_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL)
