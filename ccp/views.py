# LWYapi/ccp/views.py
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

from LWYapi import settings

from . import constant
from .models import MemberInfo
import json



def MainView(request,
             u_product="",
             u_member="",
             u_date="",
             u_process="",
             u_item="",
             u_seq="" ):

    # Change the input url to lower charector format
    u_product   = u_product.lower()
    u_member    = u_member.lower()
    u_date      = u_date.lower()
    u_process   = u_process.lower()
    u_item      = u_item.lower()
    u_seq       = u_seq.lower()


    # Call the Url Path Check
    rtUrlCheck = UrlCheckView(u_product,
                              u_member,
                              u_date,
                              u_process,
                              u_item,
                              u_seq)

    print("rtUrlCheck : "+rtUrlCheck)
    if rtUrlCheck == constant.CHECK_PRODUCT:
        return HttpResponse(constant.CHECK_PRODUCT)
    elif rtUrlCheck == constant.CHECK_MEMBER:
        return HttpResponse(constant.CHECK_MEMBER)
    elif rtUrlCheck == constant.CHECK_DATE:
        return HttpResponse(constant.CHECK_DATE)
    elif rtUrlCheck == constant.CHECK_PROCESS:
        return HttpResponse(constant.CHECK_PROCESS)
    elif rtUrlCheck == constant.CHECK_ITEM:
        return HttpResponse(constant.CHECK_ITEM)
    elif rtUrlCheck == constant.CHECK_SEQ:
        return HttpResponse(constant.CHECK_SEQ)


    # 회원정보 Check
    rtMemberCheck = MemberView(u_product, u_member)
    print (rtMemberCheck)


    # Process 별 함수 call
    if u_process == "list" :
        result = "list 호출 하셨습니다"

        RtList = ListView(  u_product ,
                            u_member ,
                            u_date ,
                            u_process ,
                            u_item )
        # result += RtList
    elif u_process == "data" :
        result = "data 호출 하셨습니다"
        RtData = DataView()
        result += RtData
    else :
        return HttpResponse("Check the u_process(:{}) ".format(u_process))




    result += "안녕하세요 ListView 클래스's " \
              " - u_product : {} " \
              " - u_member  : {} " \
              " - u_date : {} " \
              " - u_process : {} " \
              " - u_item    : {} " \
              " - u_seq     : {}" \
        .format(u_product , u_member, u_date, u_process, u_item, u_seq)



    # return HttpResponse(result)
    # return render(request, 'ccp/Result_display.html', {'result':result})
    # return render(request, 'ccp/Result_display.html', {'result':result+RtList})

    return JsonResponse(
        {
            'message': "JsonResponse Qury....." ,
            #'item': [result] ,
            'item':[u_product , u_member, u_date, u_process, u_item, u_seq],
            'LIST':[RtList]
            #
            # jsonString = json.dumps(rows , indent=4)
        } , json_dumps_params={'ensure_ascii': True}

    )



def UrlCheckView(u_product,
                 u_member,
                 u_date,
                 u_process,
                 u_item,
                 u_seq):

    # print(u_product)
    # print(u_member)
    # print(u_date)
    # print(u_process)
    # print(u_item)
    # print(u_seq)


    if u_product <= ""  or \
       u_product not in ["irs-won", "irs-usd", "ndf", "pro_fx"] :

           return constant.CHECK_PRODUCT


    if u_member <= ""   or \
       len(u_member) !=5 :
            return constant.CHECK_MEMBER


    if u_date <= ""     or \
       len(u_date) !=8 :
            return constant.CHECK_DATE

    if u_process <= ""  or \
       u_process not in ["list", "data"] :
            return constant.CHECK_PROCESS

    if u_item <= "" :
        return constant.CHECK_ITEM

    if u_seq <= "" :
        return constant.CHECK_SEQ

    return constant.CHECK_OK


# Member Authorization Checking

def MemberView(u_product, u_member):

    qs = MemberInfo.objects.all()

    qs = qs.filter(member=u_member)
    if qs.exists():
        pass
    else:
        return constant.CHECK_MEMBER


    for i in qs:
        if u_product == 'irs-won':
            if i.irs_won =='y':
                pass
            else:
                return constant.CHECK_PRODUCT

        if u_product == 'irs-usd':
            if i.irs_usd == 'y':
                pass
            else:
                return constant.CHECK_PRODUCT

        if u_product == 'ndf':
            if i.ndf == 'y':
                pass
            else:
                return constant.CHECK_PRODUCT

        if u_product == 'pro-fx':
            if i.pro_fx == 'y':
                pass
            else:
                return constant.CHECK_PRODUCT

    return constant.CHECK_OK





def ListView(u_product ,
             u_member ,
             u_date ,
             u_process ,
             u_item):

    print("- Called the ListView() ")

    # qs = MemberInfo.objects.all()
    qs = MemberInfo.objects.filter(member=u_member)


    rows = ''
    for item in qs:
        # rows = rows + "BIC_CODE : " + item.bic_code + ", "
        # jsonString = json.dumps("BIC_CIDE : " + item.bic_code)
        # rows = rows + jsonString +", "

        rows = rows + \
               'market:'        + item.market + ', '+\
               'member: '       + item.member + ', '+\
               'bic_code: '     + item.bic_code +', '+\
               'lei_code: '     + item.lei_code +', '+\
               'member_name: '  + item.member_name +', '+\
               'login_id: '     + item.login_id +', '+\
               'login_pass: '   + item.login_pass +', '+\
               'irs_won: '      + item.irs_won +', '+\
               'irs_usd: '      + item.irs_usd +', '+\
               'ndf: '          + item.ndf +', '+\
               'fx: '           + item.pro_fx+', '
        # \
        #        +\
        #        item.created_at + ""
        #


    # # q = request.GET.get('q' , '')
    # # q  = u_item.GET.get()
    # # qs = qs.filter(bic_code__icontains=u_item)


    return rows
    # return (" * Called the ListView() ")


def DataView():

    #print("- Called the DataView() ")
    return (" * Called the DataView() ")



