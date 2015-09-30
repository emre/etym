from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from base.views import IndexView, AboutView, WordCreateView, SuccessView
from base.api_views import WordViewSet

# api related
api_router = routers.DefaultRouter()
api_router.register(r'words', WordViewSet)

# django urls
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(api_router.urls)),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^add/$', WordCreateView.as_view(), name="add"),
    url(r'^add/success/$', SuccessView.as_view(), name="add-success"),
    url(r'^humans.txt/$', AboutView.as_view(), name="about"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)