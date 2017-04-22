from django.db import models


# Create your models here.

class UrlMeta(models.Model):

    market = models.CharField(max_length=20)
    product = models.CharField(max_length=20)
    member = models.CharField(max_length=20)
    process = models.CharField(max_length=20)
    item = models.CharField(max_length=20)
    seq = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)



