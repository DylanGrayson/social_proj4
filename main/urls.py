from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required as auth

from main.views.comment import LinkUpdateView
from main.views.comment import LinkDeleteView

urlpatterns = patterns('',
                       url(r'^$', 'main.views.views.home', name='home'),
                       url(r'^register/', 'main.views.register.new_user', name='newuser'),
                       url(r'^login/', 'main.views.login.user_login', name='user_login'),
                       url(r'^link/update/(?P<pk>\d+)/$', auth(LinkUpdateView.as_view()),
        name='link_update'),
                       url(r'^link/delete/(?P<pk>\d+)/$', auth(LinkDeleteView.as_view()),
        name='link_delete'),
                       url(r'^logout/', 'main.views.login.user_logout', name='user_logout'),
                       url(r'^user/(?P<num>\d+)/$', 'main.views.views.profile', name='user'),
                       url(r'^search/', 'main.views.views.search_results', name='search_results'),
                       url(r'^user/edit/(?P<num>\d+)/$', 'main.views.edit_user.edit', name='edituser'),
                       url(r'^user/addcorgi/(?P<num>\d+)/$', 'main.views.corgi.add_corgi', name='add_corgi'),
                       url(r'^user/addpost/(?P<num>\d+)/$', 'main.views.comment.add_comment', name='add_comment'),
                       url(r'^api/post/(?P<num>\d+)/$', 'main.views.api.post_list', name='api_post_list'),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
              
                       )
