# LWYapi/ccp/views.py
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from LWYapi import settings

#global i_process


def ListView(request, product="", member="", process="", item="", seq=""):

#    print("request : ", product, member, process, item, seq)

    if product > "" :
        pass
    else :
        return HttpResponse(" check the product ")

    if member > "" :
        pass
    else :
        return HttpResponse(" check the member ")

    if process > "" :
        pass
    else :
        return HttpResponse(" check the process ")

    if item > "" :
        pass
    else :
        return HttpResponse(" check the item ")

    if seq > "" :
        pass
    else :
        if process == "LIST" :
            pass
        else :
            return HttpResponse(" check the seq ")




# Process 별 함수 call
    if process == "list" :
        result = "list 호출 하셨습니다"
    elif process == "data" :
        result = "data 호출 하셨습니다"
    else :
        return HttpResponse("Check the process(:{}) ".format(process))



    result += "안녕하세요 ListView 클래스's "\
             " - Product : {} " \
             " - member  : {} " \
             " - process : {} " \
             " - item    : {} " \
             " - seq     : {}" \
             .format(product , member , process , item , seq) \

    return HttpResponse(result)




