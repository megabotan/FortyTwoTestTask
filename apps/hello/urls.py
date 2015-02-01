from django.conf.urls import patterns, url
from django.conf import settings


urlpatterns = patterns('',
    url(r'^$', 'hello.views.index', name='index'),
    url(r'^requests/$', 'hello.views.requests', name='requests'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login'),
    url(r'^edit/$', 'hello.views.edit', name='edit'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))