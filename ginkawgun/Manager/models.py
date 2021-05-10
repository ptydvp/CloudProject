from django.db import models
from django.contrib import admin
from User.models import Vendor, Customer
from django.utils.text import slugify
from django.dispatch import receiver
import os
# Create your models here.
class MyModelAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='restaurant_image', blank=True)
    address = models.TextField()
    time = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    food = 'ร้านอาหาร'
    drink = 'ร้านเครื่องดื่ม'
    res_type = (
        (food, 'food'),
        (drink, 'drink')
    )
    restaurant_type = models.CharField(
        max_length = 15,
        choices = res_type,
        default=food
    )

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s' % (self.name)

    
class Menu(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='menu_image', blank=True)
    price = models.FloatField()
    description = models.TextField()

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '(%s) %s %d %s' % (self.restaurant.name, self.name, self.price, self.description)
#Tiger#
@receiver(models.signals.post_delete, sender=Menu)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)

@receiver(models.signals.pre_save, sender=Menu)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).picture
    except sender.DoesNotExist:
        return False

    new_file = instance.picture
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
#Tiger#
class Order(models.Model):
    total_price = models.FloatField()
    payment = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    unit = models.IntegerField(default=1)
    unit_price = models.FloatField(default=False)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)

    success = 'เสร็จแล้ว'
    inprogress = 'กำลังทำ'
    cancel = 'ยกเลิก'

    status_type = (
        (success, 'success'),
        (inprogress, 'inprogress'),
        (cancel, 'cancel'),
    )
    
    status = models.CharField(
        max_length=15,
        choices=status_type,
        default=inprogress
    )

    def __str__(self):
        return '%s %s' % (self.total_price, self.payment)

class feedback(models.Model):
    date = models.DateField(auto_now_add=True)
    description = models.TextField()

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '(%s) (%s) %s' % (self.vendor.user.username, self.customer.fname, self.description)