import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from LWYapi import settings
from . import constant
from .models import MemberInfo, TOTAL_SEQ_INFO_M, IFD_POST_DATA_M
import json
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist



from django.contrib.auth import authenticate, login



#-----------------------------------------------------
# Main
#-----------------------------------------------------
# @csrf_exempt
# def my_view(request):
#     print('my_view : '+request          )
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#
#     else:
#         # Return an 'invalid login' error message.
#         pass

@csrf_exempt
def LoginView(request,
             u_login="",
             u_pass="",
              ):
    print('Accounts.LoginView{}, pass{}'.format(u_login, u_pass))


