from django.contrib import admin
from insa import views
from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'web_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.employee, name='landing'),
    url(r'input/pinfo', views.count_person, name='count'),
    url(r'input/people', views.add_person, name='add'),
    url(r'view/grade/(?P<jobID>\d+)$', views.person_main, name='show'),
    #url('/', ),
]
