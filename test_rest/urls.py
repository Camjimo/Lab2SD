from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from apprest.views import VideoViewSet, ArtistaViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'videos', VideoViewSet)
router.register(r'artistas',ArtistaViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'test_rest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^', include(router.urls)),
	url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
