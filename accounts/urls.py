#LWYapi/accounts/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^login/(?P<u_loginid>[[a-zA-Zㄱ-힣/\d/]+)/(?P<u_loginpass>[[a-zA-Zㄱ-힣/\d/]+)/$', views.LoginView),
    # [\w/\-/]+ 영어대소문자 숫자 '-', \w/{5} 5자리
    url(r'^(?P<u_username>[\w/\-/]*)/(?P<u_password>[\w/]*)/$', views.AccountsView),
    url(r'^(?P<u_username>[\w/\-/]*)/$', views.AccountsView),
    url(r'^/$', views.AccountsView),
]