from django.contrib import admin
from .models import UrlMeta, MemberInfo, TrCodeInfo_M, TOTAL_SEQ_INFO_M_, IFD_POST_DATA_M_

admin.site.register(UrlMeta)
admin.site.unregister(UrlMeta)

admin.site.register(MemberInfo)
admin.site.unregister(MemberInfo)

admin.site.register(TrCodeInfo_M)
admin.site.unregister(TrCodeInfo_M)

admin.site.register(TOTAL_SEQ_INFO_M_)
admin.site.unregister(TOTAL_SEQ_INFO_M_)


# Register your models here.

@admin.register(MemberInfo)
class MemberInfoAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at', 'login_state',
                    'market', 'member',
                    'bic_code', 'lei_code',
                    'member_name','login_id', 'login_pass',
                    'irs_won', 'irs_usd', 'ndf', 'pro_fx',
                    ]

@admin.register(UrlMeta)
class UrlMetaAdmin(admin.ModelAdmin):
    list_display = ['market', 'product', 'process', 'item', 'item_seq']

@admin.register(TrCodeInfo_M)
class TrCodeInfoAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at','market', 'member',
                    'item', 'item_group']


@admin.register(TOTAL_SEQ_INFO_M_)
class TotalSeqInfoAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at',
                    'market', 'product', 'member',
                    'item', 'item_group', 'item_seq',
                    'fmtoa_seq', 'fatob_seq', 'end_bit']

@admin.register(IFD_POST_DATA_M_)
class IfdPostDataAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at',
                    'market', 'product', 'member',
                    'item', 'item_group', 'item_seq',
                    'data']
