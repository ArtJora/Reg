from django.conf.urls import include, url


urlpatterns = [
    url(r'^login/', 'extuser.views.login'),
    url(r'^logout/', 'extuser.views.logout'),
    url(r'^register/', 'extuser.views.register'),
]
