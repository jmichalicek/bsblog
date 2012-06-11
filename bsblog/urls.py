from django.conf.urls.defaults import *
from models import Post

info_dict = {
    'queryset': Post.objects,
    'date_field': 'created_date',
}

urlpatterns = patterns('',
                       (r'^blog/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$','bsblog.views.item'),
                       (r'^blog/(?P<year>\d+)/(?P<month>[a-z]{3})/$','bsblog.views.list_posts'),
                       (r'^blog/(\d+)','bsblog.views.index'),
                       (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$',
                        'bsblog.views.item'),
                       url(r'^blog/projects/', 'bsblog.views.projects', name="projects_url"),
                       (r'^$','bsblog.views.index'),)
