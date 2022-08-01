from django.contrib import admin

from core.models import Zon,Pack,Client,Payment

# Register your models here.
class ZonAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')

class PackageAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')

class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')
    list_display = ('user','name','telephone','zon','pay_day','package')
    ordering = ('user','zon')
    search_fields = ('user','name','telephone')
    list_filter = ('zon__name','pay_day','package__name')


class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')




admin.site.register(Zon,ZonAdmin)
admin.site.register(Pack,PackageAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Payment,PaymentAdmin)
