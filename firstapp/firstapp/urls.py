from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('news.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^dancers/', include('dancers.urls')),
    url(r'^auth/', include('extuser.urls')),
    url(r'^context/', include('context.urls')),
]
