from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', 'dancers.views.dancers'),
    url(r'^adddancer/', 'dancers.views.adddancer'),
    url(r'^savedancer/', 'dancers.views.savedancer'),
    url(r'^delete/(?P<dancer_id>\d+)/$', 'dancers.views.delete_dancer'),
]