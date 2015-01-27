from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'hello.views.index', name='index'),
)