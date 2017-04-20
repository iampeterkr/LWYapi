#LWYapi/ccp/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    # [\w/\-/]+ 영어대소문자 숫자 '-', \w/{5} 5자리
    url(r'^(?P<product>[\w/\-/]+)/(?P<member>[\w/]{5})/(?P<process>[\w/]+)/(?P<item>[\w/]+)/(?P<seq>[\d]+)/$', views.ListView) ,
    url(r'^(?P<product>[\w/\-/]+)/(?P<member>[\w/]{5})/(?P<process>[\w/]+)/(?P<item>[\w/]+)/$', views.ListView) ,
    url(r'^(?P<product>[\w/\-/]+)/(?P<member>[\w/]{5})/(?P<process>[\w/]+)/$', views.ListView) ,
    url(r'^(?P<product>[\w/\-/]+)/(?P<member>[\w/]{5})/$', views.ListView) ,
    url(r'^(?P<product>[\w/\-/]+)/$', views.ListView) ,

    #url(r'^(?P<product>[a-zA-Zㄱ-힣/\d/]+)/(?P<member>[\d/]+)/$' , views.ListView) ,
    #url(r'^')
]