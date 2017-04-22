from django.db import models


# Create your models here.

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



