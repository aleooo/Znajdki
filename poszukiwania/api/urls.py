from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'rest_framework'
#
# router = routers.SimpleRouter()
# router.register(r'', views.api_overview)

urlpatterns = [
    # path('users/', views.UserList.as_view(), name='user_list'),
    # path('users/<int:id>', views.UserDetail.as_view(), name='user_detail'),
    path('', views.api_overview, name='overwiew'),
    path('list/', views.FindList.as_view(), name='finds_list'),
    path('list/<int:pk>', views.FindDetail.as_view(), name='finds_detail'),
]