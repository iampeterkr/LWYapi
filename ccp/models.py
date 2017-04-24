from django.db import models


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
    ('iw' , 'IRS-WON') ,
    ('iu' , 'IRS-USD') ,
    ('nu' , 'NDF-USD') ,
)

PROCESS_CHOICE = (
    ('list' , 'LIST') ,
    ('data' , 'DATA') ,
)

ITEM_CHOICE = (
    ('all' , 'ALL') ,
    (None , 'None') ,
)


# 회원정보 작성
class MemberInfo(models.Model):

    market = models.CharField(max_length=20, choices=MARKET_CHOICE, default="")
    member = models.CharField(max_length=20)
    bic_code = models.CharField(max_length=20)
    lei_code = models.CharField(max_length=20)
    member_name = models.CharField(max_length=20)
    login_id = models.CharField(max_length=20)
    login_pass = models.CharField(max_length=20)
    irs_won = models.CharField(max_length=3, choices=YES_NO_CHOICE, default="", null=True )
    irs_usd = models.CharField(max_length=3, choices=YES_NO_CHOICE, default="", null=True )
    ndf = models.CharField(max_length=3, choices=YES_NO_CHOICE, default="", null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    pro_fx = models.CharField(max_length=3, choices=YES_NO_CHOICE, default="", null=True )




# URL에 사용할 Meta 정보를 DB로 만듬
class UrlMeta(models.Model):

    market = models.CharField(max_length=20, choices=MARKET_CHOICE)
    product = models.CharField(max_length=20, choices=PRODUCT_CHOICE)
    member = models.CharField(max_length=20)
    process = models.CharField(max_length=20, choices=PROCESS_CHOICE)
    item = models.CharField(max_length=20, choices=ITEM_CHOICE, blank=True , null=True)
    seq = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)



