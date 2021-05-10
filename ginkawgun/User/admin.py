from webbrowser import register

from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Customer, Vendor

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','user','nphone','picture']
class VendorAdmin(admin.ModelAdmin):
    list_display = ['address','user']

admin.site.register(Permission)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Vendor,VendorAdmin)