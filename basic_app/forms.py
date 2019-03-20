from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo, Payments

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)




class PaymentsForm(forms.ModelForm):
    class Meta():
        model = Payments
        fields =('PaymentsId','id_afiliado','months','amount','payment_date')
