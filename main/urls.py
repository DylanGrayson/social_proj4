from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'main.views.main.home', name='home'),
                       url(r'^register/$', 'main.views.register.new_user', name='newuser'),
                       url(r'^admin/', include(admin.site.urls)),

                       )
