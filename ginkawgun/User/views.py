from builtins import object
from contextlib import ContextDecorator
from fnmatch import filter
from lib2to3.fixes.fix_input import context
from os.path import exists
from venv import create
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.contrib.messages.storage import session
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import F
from User.models import Customer

from .forms import ChangpassForm, RegisterForm, UserForm,Updatepicture


def app_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            customer = Customer.objects.get(user=user)
            return redirect('homepage')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password'

    return render(request, template_name='login.html',context=context)




def app_logout(request):
    logout(request)
    return redirect('login')





def edituser_form(request):
    user=request.user
    if request.method == 'POST':

        form1 = UserForm(request.POST)
        form2 = Updatepicture(request.POST, request.FILES)
        customer = Customer.objects.get(user=request.user)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        nphone = request.POST.get('nphone')

        if form1.is_valid() and form2.is_valid():
            customer.picture=request.FILES.get('picture')
            customer.save()
            User.objects.filter(username=request.user).update(first_name=fname,last_name=lname,email=email)
            Customer.objects.filter(user=request.user).update(fname=fname,lname=lname,nphone=nphone)
            return redirect('homepage')
    else:
        form1 = UserForm()
        form2 = Updatepicture(request.POST,request.FILES)

    return render(request,'edituser.html',{'form1':form1,'form2':form2})




def app_changepass(request):
    context={}
    if request.method == 'POST':
        form = ChangpassForm(request.POST)
        email = request.POST.get('email')
        username = request.POST.get('username')
        newpassword = request.POST.get('newpassword')
        if form.is_valid():
            if User.objects.filter(email=email).exists():
                print('email')
                if User.objects.filter(username=username).exists():
                    print('pass')
                    user = User.objects.get(email=email)
                    user.set_password(newpassword)
                    user.save()
                    return redirect('/login/')
                else:
                    context['form'] = form
                    context['error'] = 'Invalid Username'
            else:
                context['form'] = form
                context['error'] = 'Invalid Email'
    else:
        form = ChangpassForm()
        context={
            'form':form,
        }

    return render(request,'changepass.html',context=context)




def app_register_from(request):
    context={}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        nphone = request.POST.get('nphone')
        password = request.POST.get('password')
        password2 = request.POST.get('secpassword')
        if form.is_valid():
            print(password)
            print(password2)
            print(username)
            if password == password2:
                if User.objects.filter(username=username).exists():
                    context['form'] = form
                    context['error'] = 'Username has already been taken'
                    print("Username has already been taken")
                else:
                    if User.objects.filter(email=email).exists():
                        context['form'] = form
                        context['error'] = 'This email has already to use'
                        print("This email has already to use")
                    else:
                        user = User.objects.create_user(username, email, password)
                        user.first_name = fname
                        user.last_name = lname
                        user.save()
                        id = user.id
                        print(id)
                        coustomer = Customer.objects.create(fname = fname,lname = lname, nphone = nphone,picture = "user_image/user111.png",user_id=id)
                        count= Customer.objects.all().count()
                        print(count)
                        return redirect('/login/')
            else:
                context['form'] = form
                context['error'] = 'Password Not Match!!!'
                print("Password Not Match!!!")
    else:
        form = RegisterForm()
        context={
            'form':form,
        }

    return render(request,'register.html',context=context)
