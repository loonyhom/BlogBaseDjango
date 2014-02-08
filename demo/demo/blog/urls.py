from django.conf.urls.defaults import *
from demo.blog.views import archive

urlpatterns = patterns('',
    url(r'^$', archive),
)
