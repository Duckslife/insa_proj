from django.conf.urls import include, url
from django.contrib import admin
from insa.views import employee
urlpatterns = [
    # Examples:
    # url(r'^$', 'web_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url('/', ),
]
