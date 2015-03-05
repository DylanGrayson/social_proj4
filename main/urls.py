from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'main.views.views.home', name='home'),
                       url(r'^register/', 'main.views.register.new_user', name='newuser'),
                       url(r'^login/', 'main.views.login.user_login', name='user_login'),
                       url(r'^logout/', 'main.views.login.user_logout', name='user_logout'),
                       url(r'^user/(?P<num>\d+)/$', 'main.views.views.profile', name='user'),
                       url(r'^search/', 'main.views.views.search_results', name='search_results'),
                       url(r'^user/edit/(?P<num>\d+)/$', 'main.views.edit_user.edit', name='edituser'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
