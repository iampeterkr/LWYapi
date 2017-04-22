# LWYapi/ccp/views.py
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from LWYapi import settings
from . import constant

#global i_process

def MainView(request, product="", member="", process="", item="", seq=""):

    # call the MainView()
    rtUrlCheck = UrlCheckView(product, member, process, item, seq)

    print(rtUrlCheck)
    if rtUrlCheck :
        pass


    print("URL_PROCESS :", constant.URL_ITEM_LIST)

    print("Main/process : ", process)
    # Process 별 함수 call
    if process == "list" or process == "LIST":
        result = "list 호출 하셨습니다"
        RtList = ListView()
        result += RtList

    elif process == "data" or process == "DATA":
        result = "data 호출 하셨습니다"
        RtData = DataView()
        result += RtData
    else :
        return HttpResponse("Check the process(:{}) ".format(process))


    result += "안녕하세요 ListView 클래스's " \
              " - Product : {} " \
              " - member  : {} " \
              " - process : {} " \
              " - item    : {} " \
              " - seq     : {}" \
        .format(product , member , process , item , seq)

    return HttpResponse(result)


# def UrlCheckView(product="", member="", process="", item="", seq=""):
def UrlCheckView(product, member, process, item, seq):

    print("UrlCheckView : ", product, member, process, item, seq)

    if product > "" :
        pass
    else :
        return "CHECK_PRODUCT"

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
        if process == "LIST"  or process == "list":
            print("check seq-list")
            pass
        else :
            return HttpResponse(" check the seq: need the seq at process : DATA ")

    return True



def ListView():

    #print("- Called the ListView() ")
    return (" * Called the ListView() ")


def DataView():

    #print("- Called the DataView() ")
    return (" * Called the DataView() ")



