from django.contrib import admin
from .models import UrlMeta

admin.site.register(UrlMeta)
admin.site.unregister(UrlMeta)


# Register your models here.

@admin.register(UrlMeta)
class UrlMetaAdmin(admin.ModelAdmin):
    pass

