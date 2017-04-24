from django.db import models


# Create your models here.

# 회원정보 작성
class MemberInfo(models.Model):
    PRODUCT_CHOICE = (
        ('y' , 'YES') ,
        ('n' , 'NO') ,
    )

    market = models.CharField(max_length=20)
    member = models.CharField(max_length=20)
    bic_code = models.CharField(max_length=20)
    lei_code = models.CharField(max_length=20)
    member_name = models.CharField(max_length=20)
    login_id = models.CharField(max_length=20)
    login_pass = models.CharField(max_length=20)
    irs_won = models.CharField(max_length=1, choices=PRODUCT_CHOICE)
    irs_usd = models.CharField(max_length=1, choices=PRODUCT_CHOICE)
    ndf = models.CharField(max_length=1, choices=PRODUCT_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)




# URL에 사용할 Meta 정보를 DB로 만듬
class UrlMeta(models.Model):
    MARKET_CHOICE = (
        ('c', 'CCP'),
        ('T', 'TR'),
    )

    PRODUCT_CHOICE = (
        ('iw', 'IRS-WON'),
        ('iu', 'IRS-USD'),
        ('nu', 'NDF-USD'),
    )

    PROCESS_CHOICE = (
        ('l', 'LIST'),
        ('D', 'DATA'),
    )

    ITEM_CHOICE =(
        ('a', 'ALL'),
        ('', 'None'),
    )

    market = models.CharField(max_length=20, choices=MARKET_CHOICE)
    product = models.CharField(max_length=20, choices=PRODUCT_CHOICE)
    member = models.CharField(max_length=20)
    process = models.CharField(max_length=20, choices=PROCESS_CHOICE)
    item = models.CharField(max_length=20, choices=ITEM_CHOICE)
    seq = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)



