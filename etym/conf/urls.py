from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from base.views import IndexView, AboutView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^humans.txt/$', AboutView.as_view(), name="about"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)