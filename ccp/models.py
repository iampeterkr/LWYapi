from django.db import models

#기존 User모델을 확장
from django.contrib.auth.models import AbstractUser

from django.utils import timezone


# Create your models here.


# select 할수 있는 값 정의
MARKET_CHOICE = (
        ('ccp' , 'CCP') ,
        ('tr' , 'TR') ,
    )

YES_NO_CHOICE = (
    ('n' , 'NO') ,
    ('y' , 'YES') ,
)

PRODUCT_CHOICE = (
    ('irs-won' , 'IRS-WON') ,
    ('irs-usd' , 'IRS-USD') ,
    ('ndf' , 'NDF') ,
)

PROCESS_CHOICE = (
    ('list' , 'LIST') ,
    ('data' , 'DATA') ,
)

ITEM_CHOICE = (
    ('tcpmih00101' , 'TCPMIH00101') ,
    ('tcpmih00102' , 'TCPMIH00102') ,
    ('tcpmih00103' , 'TCPMIH00103') ,
    ('tcpmih00104' , 'TCPMIH00104') ,
    ('tcpmih00105' , 'TCPMIH00105') ,
    ('tcpmih00106' , 'TCPMIH00106') ,
    ('tcpmih00107' , 'TCPMIH00107') ,
    ('tcpmir00101' , 'TCPMIR00101') ,

)

ITEMGROUP_CHOICE = (
    ('clearing' , 'CLEARING') ,
    ('settlement' , 'SETTLEMENT') ,
    ('risk' , 'RISK') ,
    ('pricing' , 'PRICING') ,
    ('rds' , 'RDS') ,
    ('post', 'POST'),
)


# User 정보 확장
class User (AbstractUser):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    login_state = models.CharField(max_length=3, blank=True)
    market = models.CharField(max_length=20, choices=MARKET_CHOICE , default="")
    member = models.CharField(max_length=20, blank=True)
    bic_code = models.CharField(max_length=20, blank=True)
    lei_code = models.CharField(max_length=20, blank=True)
    member_name = models.CharField(max_length=50, blank=True)
    login_id = models.CharField(max_length=20, blank=True, primary_key=True)
    login_pass = models.CharField(max_length=20, blank=True)
    irs_won = models.CharField(max_length=3 , choices=YES_NO_CHOICE , default="" , null=True)
    irs_usd = models.CharField(max_length=3 , choices=YES_NO_CHOICE , default="" , null=True)
    ndf = models.CharField(max_length=3 , choices=YES_NO_CHOICE , default="" , null=True)
    pro_fx = models.CharField(max_length=3 , choices=YES_NO_CHOICE , default="" , null=True)




# 회원정보 작성
class MemberInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    login_state = models.CharField(max_length=3)
    market = models.CharField(max_length=20, choices=MARKET_CHOICE, default="")
    member = models.CharField(max_length=20)
    bic_code = models.CharField(max_length=20)
    lei_code = models.CharField(max_length=20)
    member_name = models.CharField(max_length=50)
    login_id = models.CharField(max_length=20)
    login_pass = models.CharField(max_length=20)
    irs_won = models.CharField(max_length=3, choices=YES_NO_CHOICE, default="", null=True )
    irs_usd = models.CharField(max_length=3, choices=YES_NO_CHOICE, default="", null=True )
    ndf = models.CharField(max_length=3, choices=YES_NO_CHOICE, default="", null=True )
    pro_fx = models.CharField(max_length=3, choices=YES_NO_CHOICE, default="", null=True )


# TRCODE 정보
class TrCodeInfo_M(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    market = models.CharField(max_length=20, choices=MARKET_CHOICE, default="")
    product = models.CharField(max_length=20 , choices=PRODUCT_CHOICE, default="")
    member = models.CharField(max_length=20)
    item = models.CharField(max_length=20 , choices=ITEM_CHOICE, default="")
    item_group = models.CharField(max_length=20, choices=ITEMGROUP_CHOICE, default="")


# URL에 사용할 Meta 정보를 DB로 만듬
class UrlMeta(models.Model):

    market = models.CharField(max_length=20, choices=MARKET_CHOICE)
    product = models.CharField(max_length=20, choices=PRODUCT_CHOICE)
    member = models.CharField(max_length=20)
    process = models.CharField(max_length=20, choices=PROCESS_CHOICE)
    item = models.CharField(max_length=20, choices=ITEM_CHOICE, blank=True , null=True)
    item_group = models.CharField(max_length=20 , choices=ITEMGROUP_CHOICE , default="")
    item_seq = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# 시장별 상품별 회원별 아이템 정보
class Total_Info(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    market = models.CharField(max_length=20, choices=MARKET_CHOICE, default="")
    member = models.CharField(max_length=20)
    bic_code = models.CharField(max_length=20)
    lei_code = models.CharField(max_length=20)
    member_name = models.CharField(max_length=50)
    login_id = models.CharField(max_length=20)
    login_pass = models.CharField(max_length=20)
    irs_won = models.CharField(max_length=3, choices=YES_NO_CHOICE, default="", null=True )
    irs_usd = models.CharField(max_length=3, choices=YES_NO_CHOICE, default="", null=True )
    ndf = models.CharField(max_length=3, choices=YES_NO_CHOICE, default="", null=True )
    pro_fx = models.CharField(max_length=3, choices=YES_NO_CHOICE, default="", null=True )


# 회원별 TRCODE SEQ 정보
class TOTAL_SEQ_INFO_M_(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    market = models.CharField(max_length=20, choices=MARKET_CHOICE)
    product = models.CharField(max_length=20, choices=PRODUCT_CHOICE)
    member = models.CharField(max_length=20)
    item = models.CharField(max_length=20, choices=ITEM_CHOICE, blank=True , null=True)
    item_group = models.CharField(max_length=20 , choices=ITEMGROUP_CHOICE,  blank=True , null=True)
    item_seq = models.CharField(max_length=20)
    fmtoa_seq=  models.CharField(max_length=20)
    fatob_seq = models.CharField(max_length=20)
    end_bit = models.CharField(max_length=3 , choices=YES_NO_CHOICE , default="" , null=True)


    def __str__(self):  # __unicode__ on Python 2
        return self.market


# IFD_Product_member_trcode 데이타 정보
class IFD_POST_DATA_M_(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    market = models.CharField(max_length=20, choices=MARKET_CHOICE)
    product = models.CharField(max_length=20, choices=PRODUCT_CHOICE)
    member = models.CharField(max_length=20)
    item = models.CharField(max_length=20, choices=ITEM_CHOICE, blank=True , null=True)
    item_group = models.CharField(max_length=20 , choices=ITEMGROUP_CHOICE,  blank=True , null=True)
    item_seq = models.CharField(max_length=20)
    data =  models.CharField(max_length=2000)

