from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'rest_framework'
#
# finds_list = views.FindsViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# find_detail = views.FindsViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# user_list = views.UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = [
#     path('', views.api_overview),
#     path('finds/', finds_list, name='finds-list'),
#     path('finds/<int:pk>/', find_detail, name='find-detail'),
#     path('api-auth/', user_list, name='user-list'),
#     path('api_auth/<int:pk>/', user_detail, name='user-detail'),
# ]

# router = DefaultRouter()
# router.register(r'finds', views.FindsViewSet)
# router.register(r'users', views.UserViewSet)
#
# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:id>', views.UserDetail.as_view(), name='user_detail'),
    path('list/', views.FindsList.as_view(), name='finds_list'),
    path('list/<int:pk>', views.FindsDetail.as_view(), name='finds_detail'),
]