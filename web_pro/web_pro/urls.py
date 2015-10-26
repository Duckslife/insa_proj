from django.contrib import admin
from insa import views
from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'web_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.employee, name='landing'),
    url(r'input/count', views.counter, name='count'),
    url(r'input/pinfo', views.count_person, name='info'),
    url(r'input/people', views.add_person, name='add'),
    url(r'input/grade/mark/(?P<jobID>\d+)$', views.mark_grade, name='mark'),
    url(r'input/grade/mark/res/(?P<jobID>\d+)$', views.input_mark, name='result'),
    url(r'input/grade/(?P<jobID>\d+)$', views.add_grade, name='gadd'),
    url(r'input/subnum', views.std_num, name='stdnum'),
    url(r'input/standard', views.input_std, name='stdnum'),
    url(r'view/standard', views.std_list, name='std'),
    url(r'view/grade/(?P<jobID>\d+)$', views.person_main, name='show'),
    url(r'view/dinfo/(?P<jobID>\d+)$', views.del_info, name='del'),
    #url('/', ),
]
