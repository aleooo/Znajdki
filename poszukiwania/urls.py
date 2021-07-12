from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path, reverse_lazy
from django.utils.translation import gettext_lazy as _

from . import views


app_name = 'poszukiwania'

urlpatterns = [
    path(_('add/'), views.create, name='create'),
    path(_('login/'), auth_views.LoginView.as_view(), name='login'),
    path(_('logout/'), auth_views.LogoutView.as_view(), name='logout'),
    path(_('password_change/'), auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('poszukiwania:password_change_done')), name='password_change'),
    path(_('password_change/done/'), auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path(_('password_reset/'), auth_views.PasswordResetView.as_view(success_url=reverse_lazy('poszukiwania:password_reset_done')), name='password_reset'),
    path(_('password_reset/done/'), auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(_('reset/<uidb64>/<token>/'), auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('poszukiwania:password_reset_complete')), name='password_reset_confirm'),
    path(_('reset/done/'), auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path(_('register/'), views.register, name='register'),
    path('search/', views.search, name='search'),
    path('style/', views.style, name='style'),
    path('', views.objects_list, name='objects_list'),
    path(_('delete/<int:id>/'), views.delete_objects, name='delete'),
    path(_('update/<int:id>/'), views.update, name='update'),
    path('<slug:category_slug>/', views.objects_list, name='objects_list_by_category'),
    path('<int:year>/<int:month>/<int:day>/<slug:object_slug>/<int:id>/', views.object_detail, name='object_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL)
