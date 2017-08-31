# LWYapi/ccp/views.py
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from LWYapi import settings
from . import constant
from .models import MemberInfo, TOTAL_SEQ_INFO_M_, IFD_POST_DATA_M_
import json
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist



from django.contrib.auth import authenticate, login



#-----------------------------------------------------
# Main
#-----------------------------------------------------
@csrf_exempt
def LoginView(request, u_loginid, u_loginpass):
    print('LoginView : ulogin[{}], u_loginpass[{}] '.format(u_loginid, u_loginpass))
    return HttpResponse('LoginView : ulogin[{}], u_loginpass[{}] '.format(u_loginid, u_loginpass))



    #
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

@csrf_exempt
def MainView(request,
             u_product="",
             u_member="",
             u_date="",
             u_process="",
             u_item="",
             u_seq="" ):
    print('MainView : ulogin [ request: ] ' + str(request))
    # -----------------------------------------------------
    #[공통] Change the input url to lower charector format
    # -----------------------------------------------------
    u_product   = u_product.lower()
    u_member    = u_member.lower()
    u_date      = u_date.lower()
    u_process   = u_process.lower()
    u_item      = u_item.lower()
    u_seq       = u_seq.lower()



    # -----------------------------------------------------
    #[공통] Url Path Check
    # -----------------------------------------------------
    rtUrlCheck = UrlCheckView(u_product,
                              u_member,
                              u_date,
                              u_process,
                              u_item,
                              u_seq)

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
        if u_process not in ['list']:
            return HttpResponse(constant.CHECK_SEQ)


    '''
    POST 일경우 TRCODE 만 허용
    '''
    ''' 향후 Meta 정보값을 읽어서 Check하는것으로 변경 필요 '''
    if request.method in  ['POST' , 'UPDATE' , 'DELETE']:
        if u_item in ['all', 'clearing', 'settlement', 'risk', 'rds', 'pricing']:
            return HttpResponse(constant.CHECK_ITEM)
        else:
            pass
    else:
        pass



    #-----------------------------------------------------
    #[공통] 회원정보 Check
    #-----------------------------------------------------
    rtMemberCheck = MemberCheckView(u_product, u_member)

    if rtMemberCheck == constant.CHECK_PRODUCT:
        return HttpResponse(constant.CHECK_PRODUCT + " [ product input :" + u_product +" ]")
    elif rtMemberCheck == constant.CHECK_MEMBER:
        return HttpResponse(constant.CHECK_MEMBER+ " [ member input :" + u_member + " ]")



    #-----------------------------------------------------
    #  GET , POST
    # -----------------------------------------------------
    # GET 요청
    if request.method not in ['POST', 'UPDATE', 'DELETE']:
        if u_process == "list":
            RtData = ListView(u_product ,
                              u_member ,
                              u_date ,
                              u_process ,
                              u_item)

        elif u_process == "data":
            RtData = DataView(u_product ,
                              u_member ,
                              u_date ,
                              u_process ,
                              u_item,
                              u_seq)
        else:
            return HttpResponse("Check the u_process(:{}) ".format(u_process))


        return JsonResponse(
            {
                'Message Type ': "JsonResponse Qury....." ,
                'REQUEST':
                    ['PRODUCT : ' + u_product ,
                     'MEMBER  : ' + u_member ,
                     'DATE    : ' + u_date ,
                     'PROCESS : ' + u_process ,
                     'ITEM    : ' + u_item ,
                     'SEQ     : ' + u_seq] ,
                'REPLY': [RtData.split(',')] ,

                # jsonString = json.dumps(rows , indent=4)
            } , json_dumps_params={'ensure_ascii': True}
        )
    else: #POST 요청
        content = request.POST.get('data', 'default')

        # seq duplicate check
        qs = TOTAL_SEQ_INFO_M_.objects.filter(product=u_product)
        qs = qs.filter(member=u_member)
        qs = qs.filter(item=u_item)
        qs = qs.filter(item_seq=u_seq)

        if qs:
            for item in qs:
                if item.item_seq == u_seq:
                    return HttpResponse(constant.CHECK_ITEM)
                else:
                    pass
        else:
            pass

        # No Check the Data , only checkt the received seq and next seq
        # st_content = str(content)
        # print('content : '+ st_content[0:11])

        ifd = IFD_POST_DATA_M_(
                            created_at  = u_date,
                            updated_at  = datetime.now(),
                            market      = 'ccp',
                            product     = u_product,
                            member      = u_member,
                            item        = u_item,
                            item_group  = 'item_group',
                            item_seq    = u_seq ,
                            data        = content )

        RtData = ''

        rtn = ifd.save()
        if rtn :
            RtData = 'DB save Fail[rtn:{}]'.format(rtn)
            ifd.save()
        else: #Success : return NONE

            try:
                qs = TOTAL_SEQ_INFO_M_.objects.filter(product=u_product)
                qs = qs.filter(member=u_member)
                qs = qs.get(item=u_item)
            except ObjectDoesNotExist as err:
                    print('DB Object 존재치 않음 에러')
                    RtData = 'ERROR : DB Object 존채치 않음 '
            else:
                if qs:
                    qs.update_at = datetime.now()
                    qs.save()
                    qs.item_seq = u_seq
                    qs.save()
                    qs.fmtoa_seq = u_seq
                    qs.save()

                    RtData = 'DB Save O.K [rtn:{}]'.format(rtn)
                else:
                    RtData = 'Not found the item({}) in TOTAL_SEQ_INFO_M'.format(u_item)
            finally:
                print('finally job ')


        return JsonResponse(
                    {
                    'message': "JsonResponse POST....." ,
                    'REQUEST ':
                        ['PRODUCT : ' + u_product ,
                         'MEMBER  : ' + u_member ,
                         'DATE    : ' + u_date ,
                         'PROCESS : ' + u_process ,
                         'ITEM    : ' + u_item ,
                         'SEQ     : ' + u_seq ,
                         'CONTENTS: ' + content ],
                    'REPLY': [RtData] ,
                    } , json_dumps_params={'ensure_ascii': True}
                )










'''
-----------------------------------------------------
[Function] UrlCheckView()
-----------------------------------------------------
'''
def UrlCheckView(u_product,
                 u_member,
                 u_date,
                 u_process,
                 u_item,
                 u_seq):

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
       u_process not in ["list", "data", 'create', 'delete', 'update'] :
            return constant.CHECK_PROCESS

    if u_item <= "" :
        return constant.CHECK_ITEM

    if u_seq <= "" :
        return constant.CHECK_SEQ

    return constant.CHECK_OK



'''
-----------------------------------------------------
[Function] MemberCheckView()
-----------------------------------------------------
'''
def MemberCheckView(u_product, u_member):

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



'''
-----------------------------------------------------
[Function] ListView()
-----------------------------------------------------
'''
def ListView(u_product ,
             u_member ,
             u_date ,
             u_process ,
             u_item):

    print("- Called the ListView() " + u_product)


    if u_product == 'irs-won':
        rt = IrsWonListView(u_product,
                         u_member,
                         u_date,
                         u_process,
                         u_item
                         )
    elif u_product == 'irs-usd':
        rt = IrsUsdListView(u_product,
                         u_member,
                         u_date,
                         u_process,
                         u_item)
    elif u_product == 'ndf':
        rt = NdfListView(u_product,
                         u_member,
                         u_date,
                         u_process,
                         u_item)
    elif u_product == 'fx':
        rt = FxListView(u_product,
                         u_member,
                         u_date,
                         u_process,
                         u_item)
    else:
        rt = 'Not Found (list_view(): ' + u_product

    if rt:
        return rt
    else:
        rt = 'Check the IrsWonListView() :rt : '+rt
        return rt




'''
-----------------------------------------------------
[Function] IrsWonListView()
-----------------------------------------------------
'''
def IrsWonListView(u_product,
                     u_member,
                     u_date,
                     u_process,
                     u_item):
    print("- Called the IrsWonListView() ")

    # qs = MemberInfo.objects.all().filter(member=u_member)

    rows = ''
    qs = TOTAL_SEQ_INFO_M_.objects.filter(product=u_product)
    qs = qs.filter(member=u_member)

    if u_item not in ["all" , "clearing" , "settlement" , "risk" , "pricing"]:
        qs = qs.filter(item=u_item)
        if qs:
            for item in qs:
                rows = rows + \
                       'Date:' + str(item.created_at) + ',' + \
                       'Market:' + item.market + ',' + \
                       'Product:' + item.product + ',' + \
                       'Member:' + item.member + ',' + \
                       'Item:' + item.item + ',' + \
                       'Item_Group:' + item.item_group + ',' + \
                       'Item_Seq:' + item.item_seq + ',' + \
                       'End_Bit:' + item.end_bit + ','
        else:
            rows = 'Not Found : ' + u_item
    elif u_item == 'all':
        #qs = TOTAL_SEQ_INFO_M_.objects.filter(member=u_member)
        if qs:
            for item in qs:
                rows = rows + \
                       'Date:' + str(item.created_at) + ',' + \
                       'Market:' + item.market + ',' + \
                       'Product:' + item.product + ',' + \
                       'Member:' + item.member + ',' + \
                       'Item:' + item.item + ',' + \
                       'Item_Group:' + item.item_group + ',' + \
                       'Item_Seq:' + item.item_seq + ',' + \
                       'End_Bit:' + item.end_bit + ','
        else:
            rows = 'Not Found : ' + u_item
    else:  # Get the 'item_group'
        qs = qs.filter(item_group =u_item)
        for item in qs:
            if item.item_group:
                rows = rows + \
                       'Date:' + str(item.created_at) + ',' + \
                       'Market:' + item.market + ',' + \
                       'Product:' + item.product + ',' + \
                       'Member:' + item.member + ',' + \
                       'Item:' + item.item + ',' + \
                       'Item_Group:' + item.item_group + ',' + \
                       'Item_Seq:' + item.item_seq + ',' + \
                       'End_Bit:' + item.end_bit + ','
            else:
                rows = 'Not Found, Group Item: ' + u_item


                # rows = rows + "BIC_CODE : " + item.bic_code + ", "
                # jsonString = json.dumps("BIC_CIDE : " + item.bic_code)
                # rows = rows + jsonString +", "
                # rows = rows + item.get_market_display()



                # \
                #        +\
                #        item.created_at + ""
                #

    # # q = request.GET.get('q' , '')
    # # q  = u_item.GET.get()
    # # qs = qs.filter(bic_code__icontains=u_item)


    return rows


    # return (" * Called the ListView() ")



'''
-----------------------------------------------------
[Function] DataView()
-----------------------------------------------------
'''
def DataView(u_product, u_member, u_date, u_process, u_item, u_seq):

    if u_product == 'irs-won':
        rt = IrsWonDataView(u_product ,
                            u_member ,
                            u_date ,
                            u_process ,
                            u_item,
                            u_seq)
    elif u_product == 'irs-usd':
        rt = IrsUsdDataView(u_product ,
                            u_member ,
                            u_date ,
                            u_process ,
                            u_item,
                            u_seq)
    elif u_product == 'ndf':
        rt = NdfDataView(u_product ,
                         u_member ,
                         u_date ,
                         u_process ,
                         u_item,
                         u_seq)
    elif u_product == 'fx':
        rt = FxDataView(u_product ,
                        u_member ,
                        u_date ,
                        u_process ,
                        u_item,
                        u_seq)
    else:
        rt = 'Not Found (Dist_view(): ' + u_product

    if rt:
        return rt
    else:
        rt = 'Check the ListVie() :rt : ' + rt
        return rt



'''
-----------------------------------------------------
[Function] IrsWonListView()
-----------------------------------------------------
'''
def IrsWonListView(u_product,
                     u_member,
                     u_date,
                     u_process,
                     u_item):
    print("- Called the IrsWonListView() ")

    # qs = MemberInfo.objects.all().filter(member=u_member)

    rows = ''
    qs = TOTAL_SEQ_INFO_M_.objects.filter(product=u_product)
    qs = qs.filter(member=u_member)

    if u_item not in ["all" , "clearing" , "settlement" , "risk" , "pricing"]:
        qs = qs.filter(item=u_item)
        if qs:
            for item in qs:
                rows = rows + \
                       'Date:' + str(item.created_at) + ',' + \
                       'Market:' + item.market + ',' + \
                       'Product:' + item.product + ',' + \
                       'Member:' + item.member + ',' + \
                       'Item:' + item.item + ',' + \
                       'Item_Group:' + item.item_group + ',' + \
                       'Item_Seq:' + item.item_seq + ',' + \
                       'End_Bit:' + item.end_bit + ','
        else:
            rows = 'Not Found : ' + u_item
    elif u_item == 'all':
        #qs = TOTAL_SEQ_INFO_M_.objects.filter(member=u_member)
        if qs:
            for item in qs:
                rows = rows + \
                       'Date:' + str(item.created_at) + ',' + \
                       'Market:' + item.market + ',' + \
                       'Product:' + item.product + ',' + \
                       'Member:' + item.member + ',' + \
                       'Item:' + item.item + ',' + \
                       'Item_Group:' + item.item_group + ',' + \
                       'Item_Seq:' + item.item_seq + ',' + \
                       'End_Bit:' + item.end_bit + ','
        else:
            rows = 'Not Found : ' + u_item
    else:  # Get the 'item_group'
        qs = qs.filter(item_group =u_item)
        for item in qs:
            if item.item_group:
                rows = rows + \
                       'Date:' + str(item.created_at) + ',' + \
                       'Market:' + item.market + ',' + \
                       'Product:' + item.product + ',' + \
                       'Member:' + item.member + ',' + \
                       'Item:' + item.item + ',' + \
                       'Item_Group:' + item.item_group + ',' + \
                       'Item_Seq:' + item.item_seq + ',' + \
                       'End_Bit:' + item.end_bit + ','
            else:
                rows = 'Not Found, Group Item: ' + u_item


                # rows = rows + "BIC_CODE : " + item.bic_code + ", "
                # jsonString = json.dumps("BIC_CIDE : " + item.bic_code)
                # rows = rows + jsonString +", "
                # rows = rows + item.get_market_display()



                # \
                #        +\
                #        item.created_at + ""
                #

    # # q = request.GET.get('q' , '')
    # # q  = u_item.GET.get()
    # # qs = qs.filter(bic_code__icontains=u_item)


    return rows


    # return (" * Called the ListView() ")



'''
-----------------------------------------------------
[Function] IrsUsdListView()
-----------------------------------------------------
'''
def IrsUsdListView(u_product,
                     u_member,
                     u_date,
                     u_process,
                     u_item):
    #print("- Called the IrsUsdListView() ")
    return (" * Called the IrsUsdListView() ")




'''
-----------------------------------------------------
[Function] NdfListView()
-----------------------------------------------------
'''
def NdfListView(u_product,
                     u_member,
                     u_date,
                     u_process,
                     u_item):
    #print("- Called the NdfListView() ")
    return (" * Called the NdfListView() ")



'''
-----------------------------------------------------
[Function] FxListView()
-----------------------------------------------------
'''
def FxListView(u_product,
                     u_member,
                     u_date,
                     u_process,
                     u_item):
    #print("- Called the FxListView() ")
    return (" * Called the FxListView() ")




'''
-----------------------------------------------------
[Function] IrsWonDataView()
-----------------------------------------------------
'''
def IrsWonDataView(  u_product,
                     u_member,
                     u_date,
                     u_process,
                     u_item,
                     u_seq):
    print("- Called the IrsWonDataView() ")

    rows = ''
    qs = IFD_POST_DATA_M_.objects.filter(product=u_product)
    qs = qs.filter(member=u_member)

    if u_item not in ["all" , "clearing" , "settlement" , "risk" , "pricing"]:
        qs = qs.filter(item=u_item)
        if qs:
            for item in qs:
                rows = rows + \
                       'Date:' + str(item.created_at) + ',' + \
                       'Market:' + item.market + ',' + \
                       'Product:' + item.product + ',' + \
                       'Member:' + item.member + ',' + \
                       'Item:' + item.item + ',' + \
                       'Item_Group:' + item.item_group + ',' + \
                       'Item_Seq:' + item.item_seq + ',' + \
                       'Data:' + item.data + ','
        else:
            rows = 'Not Found : ' + u_item
    elif u_item == 'all':
        if qs:
            for item in qs:
                rows = rows + \
                       'Date:' + str(item.created_at) + ',' + \
                       'Market:' + item.market + ',' + \
                       'Product:' + item.product + ',' + \
                       'Member:' + item.member + ',' + \
                       'Item:' + item.item + ',' + \
                       'Item_Group:' + item.item_group + ',' + \
                       'Item_Seq:' + item.item_seq + ',' + \
                       'Data:' + item.data + ','
        else:
            rows = 'Not Found : ' + u_item
    else:  # Get the 'item_group'
        qs = qs.filter(item_group =u_item)
        for item in qs:
            if item.item_group:
                rows = rows + \
                       'Date:' + str(item.created_at) + ',' + \
                       'Market:' + item.market + ',' + \
                       'Product:' + item.product + ',' + \
                       'Member:' + item.member + ',' + \
                       'Item:' + item.item + ',' + \
                       'Item_Group:' + item.item_group + ',' + \
                       'Item_Seq:' + item.item_seq + ',' + \
                       'Data:' + item.data + ','
            else:
                rows = 'Not Found, Group Item: ' + u_item


                # rows = rows + "BIC_CODE : " + item.bic_code + ", "
                # jsonString = json.dumps("BIC_CIDE : " + item.bic_code)
                # rows = rows + jsonString +", "
                # rows = rows + item.get_market_display()



                # \
                #        +\
                #        item.created_at + ""
                #

    # # q = request.GET.get('q' , '')
    # # q  = u_item.GET.get()
    # # qs = qs.filter(bic_code__icontains=u_item)


    return rows


    # return (" * Called the ListView() ")





'''
-----------------------------------------------------
[Function] IrsUsdDataView()
-----------------------------------------------------
'''
def IrsUsdDataView(  u_product,
                     u_member,
                     u_date,
                     u_process,
                     u_item,
                     u_seq):
    print("- Called the IrsUsdDataView() ")




'''
-----------------------------------------------------
[Function] NdfDataView()
-----------------------------------------------------
'''
def NdfDataView(  u_product,
                     u_member,
                     u_date,
                     u_process,
                     u_item,
                     u_seq):
    print("- Called the NdfDataView() ")





'''
-----------------------------------------------------
[Function] FxDataView()
-----------------------------------------------------
'''
def FxDataView(  u_product,
                     u_member,
                     u_date,
                     u_process,
                     u_item,
                     u_seq):
    print("- Called the FxDataView() ")
