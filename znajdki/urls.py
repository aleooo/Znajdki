from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('poszukiwania.api.urls', namespace='rest_framework')),
    path('rosetta/', include('rosetta.urls')),
    path('', include('poszukiwania.urls', namespace='poszukiwania')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL)