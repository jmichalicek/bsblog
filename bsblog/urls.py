from django.conf.urls.defaults import *
from models import Post

info_dict = {
    'queryset': Post.objects,
    'date_field': 'created_date',
}

urlpatterns = patterns('',
                       url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$',
                           'bsblog.views.item', name='bsblog_full_post_url'),
                       url(r'^blog/(?P<year>\d+)/(?P<month>[a-z]{3})/$','bsblog.views.list_posts'),
                       url(r'^blog/(\d+)','bsblog.views.index'),
                       url(r'^projects/', 'bsblog.views.projects', name="projects_url"),
                       url(r'^$','bsblog.views.index', name='bsblog_main'),)
