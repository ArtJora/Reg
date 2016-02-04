from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', 'news.views.news'),
    url(r'^(?P<article_id>\d+)/$', 'news.views.news_item'),
    url(r'^addlike/(?P<article_id>\d+)/$', 'news.views.addlike'),
    url(r'^addcomment/(?P<article_id>\d+)/$', 'news.views.addcomment'),
    url(r'^savenews/$', 'news.views.savenews'),
    url(r'^addnews/$', 'news.views.addnews'),

]
