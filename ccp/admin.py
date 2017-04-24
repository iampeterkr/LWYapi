from django.contrib import admin
from .models import UrlMeta, MemberInfo

admin.site.register(UrlMeta)
admin.site.unregister(UrlMeta)

admin.site.register(MemberInfo)
admin.site.unregister(MemberInfo)


# Register your models here.

@admin.register(MemberInfo)
class MemberInfoAdmin(admin.ModelAdmin):
    list_display = ['market', 'member', 'bic_code', 'lei_code',
                    'member_name','login_id', 'login_pass',
                    'irs_won', 'irs_usd', 'ndf', 'pro_fx',
                    'created_at', 'updated_at']

@admin.register(UrlMeta)
class UrlMetaAdmin(admin.ModelAdmin):
    list_display = ['market', 'product', 'process', 'item', 'seq']

