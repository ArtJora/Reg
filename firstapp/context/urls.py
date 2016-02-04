from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', 'context.views.contexts'),
    url(r'addcontext/$', 'context.views.addcontext'),
    url(r'dancers/$', 'context.views.context_dancers'),
    url(r'^(?P<context_id>\d+)/$', 'context.views.context_dancers'),
    url(r'^delete/(?P<context_id>\d+)/(?P<dancer_id>\d+)/$', 'context.views.delete_dancers'),
    url(r'^search/$', 'context.views.search_dancer'),
    url(r'^search_dance_program/$', 'context.views.search_dance_program'),
    url(r'^search_age_category/$', 'context.views.search_age_category'),
    url(r'^search_dance_league/$', 'context.views.search_dance_league'),
    url(r'^(?P<context_id>\d+)/addsolo/$', 'context.views.addsolo'),
    url(r'^(?P<context_id>\d+)/addduet/$', 'context.views.addduet'),
    url(r'^(?P<context_id>\d+)/addgruppa/$', 'context.views.addgruppa'),
]
