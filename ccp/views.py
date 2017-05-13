# LWYapi/ccp/views.py
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from LWYapi import settings

from . import constant


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

    # Process 별 함수 call
    if u_process == "list" :
        result = "list 호출 하셨습니다"
        RtList = ListView()
        result += RtList

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

    return HttpResponse(result)


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
       u_product not in ["irs-won", "irs-usd", "ndf"] :
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


def ListView():

    #print("- Called the ListView() ")
    return (" * Called the ListView() ")


def DataView():

    #print("- Called the DataView() ")
    return (" * Called the DataView() ")



