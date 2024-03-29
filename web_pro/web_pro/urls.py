from django.contrib import admin
from insa import views
from insa.views import *
from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'web_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.employee, name='landing'),
    url(r'input/count', views.counter, name='count'),
    url(r'input/pinfo', count_person, name='info'),
    url(r'input/people', UserInfo.add_person, name='add'),
    url(r'input/grade/mark/(?P<jobID>\d+)$', views.mark_grade, name='mark'),
    url(r'input/grade/mark/res/(?P<jobID>\d+)$', views.input_mark, name='result'),
    url(r'input/grade/(?P<jobID>\d+)$', views.add_grade, name='gadd'),
    url(r'input/subnum', views.std_num, name='stdnum'),
    url(r'input/std_subnum', views.ag_std_num, name='stdsubnum'),
    url(r'input/standard', views.input_std, name='instd'),
    url(r'view/standard', views.std_list, name='std'),
    url(r'view/grade/(?P<jobID>\d+)$', UserInfo.person_main, name='show'),
    url(r'view/dinfo/(?P<jobID>\d+)$', UserInfo.del_info, name='del'),
    url(r'diff/std/(?P<subject>\w{0,50})?$', views.upd_std, name='mstd'),
    url(r'diff/std/modif/(?P<subject>\w{0,50})?$', views.mod_std, name='cmstd'),
    #url('/', ),
]
