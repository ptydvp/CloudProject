from django.contrib import admin
from .models import Restaurant,Order,feedback,Menu
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name','picture','address','time','phone','res_type','vendor']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['total_price','payment','datetime']
class feedbackAdmin(admin.ModelAdmin):
    list_display = ['date','description','vendor','customer']
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name','picture','price','description','restaurant']

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(feedback,feedbackAdmin)
admin.site.register(Menu,MenuAdmin)