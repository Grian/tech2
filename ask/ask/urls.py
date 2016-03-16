from django.conf.urls import patterns, include, url
from django.contrib import admin
from qa.views import test,tt,question,main_pager, popular_pager
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_pager),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(\d+)/', question, name='question-item'),
    url(r'^ask/', test),
    url(r'^popular/', popular_pager),
    url(r'^new/', test),
    url(r'^tt/', tt),
)
