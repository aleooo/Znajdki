from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _


urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path(_('api/'), include('poszukiwania.api.urls', namespace='rest_framework')),
    path(_('rosetta/'), include('rosetta.urls')),
    path('', include('poszukiwania.urls', namespace='poszukiwania')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL)
