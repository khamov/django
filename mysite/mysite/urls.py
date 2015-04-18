from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello,cur_date,hour_ahead

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
   url(r'^hello/$',hello),
   url(r'^time/$',cur_date),
   url(r'^time/plus/(\d{1,2})/$',hour_ahead)
]
