from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from app01.views import home


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/', home.index),
    url(r'^$', home.index),
    url(r'^show_message', home.show_message),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/index/$', 'blog.views.index'),
    url(r'^auth/', home.auth),

)
