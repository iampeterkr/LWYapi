#LWYapi/ccp/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    # [\w/\-/]+ 영어대소문자 숫자 '-', \w/{5} 5자리
    url(r'^(?P<u_product>[\w/\-/]+)/(?P<u_member>[\w/]+)/(?P<u_date>[\d]+)/(?P<u_process>[\w/]+)/(?P<u_item>[\w/]+)/(?P<u_seq>[\d]+)/$', views.MainView) ,
    url(r'^(?P<u_product>[\w/\-/]+)/(?P<u_member>[\w/]+)/(?P<u_date>[\d]+)/(?P<u_process>[\w/]+)/(?P<u_item>[\w/]+)/$', views.MainView) ,
    url(r'^(?P<u_product>[\w/\-/]+)/(?P<u_member>[\w/]+)/(?P<u_date>[\d]+)/(?P<u_process>[\w/]+)/$', views.MainView) ,
    url(r'^(?P<u_product>[\w/\-/]+)/(?P<u_member>[\w/]+)/(?P<u_date>[\d]+)/$', views.MainView) ,
    url(r'^(?P<u_product>[\w/\-/]+)/(?P<u_member>[\w/]+)/$', views.MainView) ,
    url(r'^(?P<u_product>[\w/\-/]+)/$' , views.MainView) ,
    url(r'^', views.MainView) ,
    # '/'를 붙여주고 안 붙여 주는것을 완벽히 이해가 안되어 있음

    #url(r'^(?P<product>[a-zA-Zㄱ-힣/\d/]+)/(?P<u_member>[\d/]+)/$' , views.ListView) ,
    #url(r'^')
]