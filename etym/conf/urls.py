from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from base.views import IndexView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name="index"),
]

from django.conf import settings


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)