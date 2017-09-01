# Create your views here.
# LWYapi/accounts/views.py
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from LWYapi import settings
from ccp import constant
from ccp.models import MemberInfo
import json
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from ccp.views import MemberCheckView



from django.contrib.auth import authenticate, login



#-----------------------------------------------------
# Main
#-----------------------------------------------------

@csrf_exempt
def AccountsView(request, u_username="", u_password=''):
    print('AccountsView : u_username[{}], u_password[{}] '.format(u_username, u_password))

    # POST로 로그인 하는 기능은 조금있다가 업그레이드 현재는 GET로 설정
    # product / ~~` username:aaa, userpass:bbb
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     # Redirect to a success page.
    #
    # else:
    #     # Return an 'invalid login' error message.
    #     pass


    #u_username  = u_username.lower()
    #u_password  = u_password.lower()

    if u_username <= ""  or u_password <= "" :
        return JsonResponse(
                {
                'Message Type ': "JsonResponse Qury....." ,
                'REQUEST':
                    ['USERNAME : ' + u_username,
                     'PASSWORD : ' + u_password,],
                'REPLY':
                    [constant.CHECK_ACCOUNTS],
                } , json_dumps_params={'ensure_ascii': True}
            )
    else:
        pass


    qs = MemberInfo.objects.all()
    qs = qs.filter(login_id=u_username)

    if qs.exists():
        #login_stat 값 No->YES 변경
        RtData=MemberInfoUpdateView(u_username)

        if RtData:
            return JsonResponse(
                {
                    'message': "JsonResponse POST....." ,
                    'REQUEST ':
                        ['USERNAME : ' + u_username ,
                         'PASSWORD : ' + u_password , ] ,
                    'REPLY': [RtData.split(',')] ,
                } , json_dumps_params={'ensure_ascii': True}
            )
        else:
            return JsonResponse(
                {
                    'Message Type ': "JsonResponse Qury....." ,
                    'REQUEST':
                        ['USERNAME : ' + u_username ,
                         'PASSWORD : ' + u_password , ] ,
                    'REPLY':
                        [constant.CHECK_ACCOUNTS] ,
                } , json_dumps_params={'ensure_ascii': True}
            )
    else:
        return JsonResponse(
                {
                'Message Type ': "JsonResponse Qury....." ,
                'REQUEST':
                    ['USERNAME : ' + u_username,
                     'PASSWORD : ' + u_password,],
                'REPLY':
                    [constant.CHECK_ACCOUNTS],
                } , json_dumps_params={'ensure_ascii': True}
            )


def MemberInfoUpdateView( u_username):

    rows = ''
    qs = MemberInfo.objects.all()
    qs = qs.get(login_id=u_username)

    qs.update_at = datetime.now()
    qs.save()
    qs.login_state = 'YES'
    qs.save()

    qs = MemberInfo.objects.filter(login_id=u_username)
    for item in qs:
        rows = rows + \
               'Date:' + str(item.updated_at) + ',' + \
               'LoginState:' + item.login_state + ',' + \
               'Market:' + item.market + ',' + \
               'Member:' + item.member + ',' + \
               'MemberName:' + item.member_name + ',' + \
               'BicCode:'+ item.bic_code + ',' + \
               'LeiCode:' + item.lei_code + ',' + \
               'IrsWon:' + item.irs_won + ',' + \
               'IrsUsd:' + item.irs_usd + ',' + \
               'NDF:' + item.ndf + ',' + \
               'ProFx:' + item.pro_fx + ','

    return rows


