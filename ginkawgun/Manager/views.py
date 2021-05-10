import json
from builtins import object
from fnmatch import filter
from idlelib import debugger
from itertools import count
from optparse import Values
from os.path import getatime, pardir
from urllib import request
from venv import create

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.storage import session
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.context_processors import request
from pkg_resources import require

from Manager.models import *
from User.models import *


def app_homepage(request):
    user = request.user
    user_all = Customer.objects.all()
    menu_list = Menu.objects.all()
    user.has_perm('sites.change_site')
    if request.user.is_authenticated:
        user=request.user
        #getfilter
        customer = Customer.objects.get(user=request.user)

        print(user.id)
        try:
            # res_list = Restaurant.objects.get(vendor_id=user.id)
            res_list = Restaurant.objects.all()
        except:
            res_list = Restaurant.objects.all()
        orderlist = Order.objects.filter(customer_id=request.user.id)
        orderall = Order.objects.all()
        request.session['phone'] = customer.nphone
        request.session['img'] = str(customer.picture)
        context = {
        'res_list': res_list,
        'user_all': user_all,
        'menu_list': menu_list,
        'orderlist': orderlist,
        'orderall': orderall
        }
    else:
        context = {
        'user_all': user_all,
        'menu_list': menu_list,
        }

    #search
    search = request.GET.get('search', '')
    if search != '':
        menu_list = Menu.objects.filter(name__icontains=search)
    return render(request, template_name='home.html', context=context)

def menu_list(request, res_id):
    res = Restaurant.objects.get(pk=res_id)
    menu_list = Menu.objects.filter(restaurant__id=res_id)
    context = {
        'res': res,
        'menu_list': menu_list,
    }

    return render(request, template_name='menu.html', context=context)




#Tiger####
@login_required
def app_add_food(request):
    user = request.user
    vid = Vendor.objects.get(pk=user.id)
    if request.method == 'POST':
        newfood = Menu.objects.create(
            name=request.POST.get('fname'),
            picture=request.FILES.get('file-input'),
            price=request.POST.get('fprice'),
            description=request.POST.get('fdescription'),
            restaurant = Restaurant.objects.get(vendor_id=vid.user_id),

        )
    else:
        newfood =  Menu.objects.none()
    
    context = {
        'newfood': newfood,
    }
    return render(request, template_name='add_food.html', context=context)

@login_required
def app_update_food(request):
    user = request.user
    vid = Vendor.objects.get(pk=user.id)
    restaurant = Restaurant.objects.get(vendor_id=vid.user_id)
    food = Menu.objects.filter(restaurant_id=restaurant.id)
    
    context = {
        'food': food,
        'restaurant' : restaurant,
    }


    return render(request, template_name='update_food.html', context=context)    

@login_required
def menu_update(request, menu_id):
    try:
        menu = Menu.objects.get(pk=menu_id)
    except Menu.DoesNotExist:
        return redirect('update_food')
    if request.method == 'POST':
        menu.name=request.POST.get('fname')
        image = request.FILES.get('file-input')
        if request.FILES.get('file-input') != None:
            menu.picture=request.FILES.get('file-input')
        menu.price=request.POST.get('fprice')
        menu.description=request.POST.get('fdescription')
        menu.save()
        return redirect(to='update_food')
    context = {
        'menu': menu,
    }

    
    return render(request, template_name='menu_update.html', context=context)   

@login_required
def menu_delete(request, menu_id):
    menu = Menu.objects.get(pk=menu_id)
    menu.delete()
    user = request.user
    return redirect(to='update_food')

#P
@login_required
def add_cart(request, menu_id):
    user=request.user
    customer = Customer.objects.get(user=request.user)
    menu = Menu.objects.get(pk=menu_id)
    order = Order.objects.create(total_price=menu.price,payment='None',unit=1,unit_price=menu.price,customer_id=customer.user_id,menu_id=menu.id,restaurant_id=menu.restaurant_id,status='inprogress')
    return redirect(to='homepage') 

def delete_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.delete()
    return redirect(to='homepage')

def success_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order = Order.objects.update(
        status = 'success'
    )
    return redirect(to='homepage')

def plus_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order = Order.objects.update(
        unit = order.unit + 1,
        total_price = order.menu.price + order.menu.price
    )
    return redirect(to='homepage')

def minus_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order = Order.objects.update(
        unit = order.unit - 1,
        total_price = order.menu.price - order.menu.price
    )
    return redirect(to='homepage')

@login_required
def payment(request):
    user = request.user
    context = {

    }

    return render(request, template_name='payment.html', context=context)

def Feedback(request, ven_id):
    feed = feedback.objects.filter(vendor=ven_id)
    current_user = request.user
    feed_data = feedback.objects.filter(vendor__user__id=ven_id)
    comment = request.GET.get('comment', '')
    if comment != '':
        new_feedback = feedback.objects.create(
            description = comment,
            vendor = ven_id,
            customer = current_user,
        )

    return render(request, template_name='feedback.html', context={
        'feed': feed,
        'feed_data': feed_data,
    })