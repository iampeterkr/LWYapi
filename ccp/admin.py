from django.contrib import admin, auth
from .models import User, UrlMeta, MemberInfo, TrCodeInfo_M, TOTAL_SEQ_INFO_M, IFD_POST_DATA_M, IFD_BIZ_DATA_M


admin.site.register(User)
admin.site.unregister(User)

admin.site.register(UrlMeta)
admin.site.unregister(UrlMeta)

admin.site.register(MemberInfo)
admin.site.unregister(MemberInfo)

admin.site.register(TrCodeInfo_M)
admin.site.unregister(TrCodeInfo_M)

admin.site.register(TOTAL_SEQ_INFO_M)
admin.site.unregister(TOTAL_SEQ_INFO_M)

admin.site.register(IFD_POST_DATA_M)
admin.site.unregister(IFD_POST_DATA_M)

admin.site.register(IFD_BIZ_DATA_M)
admin.site.unregister(IFD_BIZ_DATA_M)


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'login_state']
    #list_display = ['id', 'username', 'password']

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


@admin.register(TOTAL_SEQ_INFO_M)
class TotalSeqInfoAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at',
                    'market', 'product', 'member',
                    'item', 'item_group', 'item_seq',
                    'fmtoa_seq', 'fatob_seq', 'end_bit']

@admin.register(IFD_POST_DATA_M)
class IfdPostDataAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at',
                    'market', 'product', 'member',
                    'item', 'item_group', 'item_seq',
                    'data']

@admin.register(IFD_BIZ_DATA_M)
class IfdBizDataAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at',
                    'market', 'product', 'member',
                    'item', 'item_group', 'item_seq',
                    'data']
