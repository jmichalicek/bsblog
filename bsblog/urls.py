from django.conf.urls.defaults import *
from models import Post

info_dict = {
    'queryset': Post.objects,
    'date_field': 'created_date',
}

urlpatterns = patterns('',
                       (r'^blog/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$','bscms.views.item'),
                       (r'^blog/(?P<year>\d+)/(?P<month>[a-z]{3})/$','bscms.views.list_posts'),
                       (r'^blog/(\d+)','bscms.views.index'),
                       (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$',
                        'bscms.views.item'),
                       url(r'^blog/projects/', 'bscms.views.projects', name="projects_url"),
                       (r'^$','bscms.views.index'),)
