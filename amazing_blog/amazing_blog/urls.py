from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog.views import PostList, PostDetail, PostUpdate, PostDelete

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'amazing_blog.views.home', name='home'),
    # url(r'^amazing_blog/', include('amazing_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'post/(?P<pk>\d+)/edit$', PostUpdate.as_view(), name='post_update'),
    url(r'post/(?P<pk>\d+)/delete$', PostDelete.as_view(), name='post_delete'),
    url(r'post/(?P<pk>\d+)$', PostDetail.as_view(), name="post_detail"),
    url(r'$', PostList.as_view(), name="post_list"),
)
