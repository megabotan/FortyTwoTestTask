from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'hello.views.index', name='index'),
    url(r'^requests/$', 'hello.views.requests', name='requests'),
)