from django.conf.urls.defaults import patterns, url

from tapz import views

urlpatterns = patterns('',
    url(r'^(?P<event_type>[0-9a-zA-Z_-]+)/(?P<sub_call>[0-9a-zA-Z_-]+)/$', views.index, name='tapz-sub-panel'),
    url(r'^(?P<event_type>[0-9a-zA-Z_-]+)/$', views.index, name='tapz-panel'),
    url(r'^$', views.index, name='tapz-index'),
)
