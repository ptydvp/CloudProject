from dataclasses import field, fields

from django import forms
from django.forms import ModelForm

from .models import Customer


class Updatepicture(ModelForm):
    class Meta:
        model = Customer
        fields = ['picture']
        
class UserForm(forms.Form):
    fname  = forms.CharField(max_length=50)
    lname = forms.CharField(max_length=50)
    email = forms.EmailField()
    nphone = forms.CharField(max_length=10,min_length=10,required=True)
    fname.widget.attrs.update({'class':'input--style-5','type':"text",'name':"fname",'style':'width:100%;','placeholder':"First Name"})
    lname.widget.attrs.update({'class':'input--style-5','type':"text",'name':"lname",'style':'width:100%;','placeholder':"Lastname Name"})
    email.widget.attrs.update({'class': 'input--style-5','type':"email",'name':"email"})
    nphone.widget.attrs.update({'class': 'input--style-5','type':"text",'name':"nphone",'pattern':"[0-9]{1,}","title":"กรอกเบอร์มือถือให้ถูกต้อง","placeholder":"Please enter your PhoneNumber 0-9"})

class ChangpassForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=50,required=True)
    newpassword = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput)
    email.widget.attrs.update({'class': 'input--style-5','type':"email",'name':"email",'style':'width:400px;'})
    username.widget.attrs.update({'class': 'input--style-5','type':"username",'name':"username",'style':'width:400px;'})
    newpassword.widget.attrs.update({'class':'input--style-5','type':"text",'name':"newpassword",'style':'width:400px;'})

class RegisterForm(forms.Form):
    fname  = forms.CharField(max_length=50,required=True)
    lname = forms.CharField(max_length=50,required=True)
    username = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput)
    secpassword = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput)
    nphone = forms.CharField(max_length=10,min_length=10,required=True)
    fname.widget.attrs.update({'class':'input--style-5','type':"text",'name':"fname",'style':'width:100%;','placeholder':"First Name"})
    lname.widget.attrs.update({'class':'input--style-5','type':"text",'name':"lname",'style':'width:100%;','placeholder':"Lastname Name"})
    username.widget.attrs.update({'class': 'input--style-5','type':"username",'name':"username"})
    email.widget.attrs.update({'class': 'input--style-5','type':"email",'name':"email"})
    password.widget.attrs.update({'class': 'input--style-5',"type":"password",'name':"password"})
    secpassword.widget.attrs.update({'class': 'input--style-5',"type":"password",'name':"secpassword",'placeholder':"Please enter your password again"})
    nphone.widget.attrs.update({'class': 'input--style-5','type':"text",'name':"nphone",'pattern':"[0-9]{1,}","title":"กรอกเบอร์มือถือให้ถูกต้อง","placeholder":"Please enter your PhoneNumber 0-9"})
