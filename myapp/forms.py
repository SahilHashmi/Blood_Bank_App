from dataclasses import fields
from django import forms
from . import models


userTypes=[('Admin','admin'),('BloodBank','bloodbank')]

class MyUserForm(forms.ModelForm):
     firstname=forms.CharField()
     lastname=forms.CharField()
     username=forms.CharField()
     password=forms.CharField(widget=forms.PasswordInput)
     usertype=forms.CharField(widget=forms.Select(choices=userTypes))
     class Meta:
         model=models.MyUser
         fields="__all__"

class BloodBankForms(forms.ModelForm):
    class Meta:
        model=models.Bloodbank
        fields="__all__"

class DonorForm(forms.ModelForm):
    class Meta:
        model=models.Donor
        fields="__all__"

class ReceiverForms(forms.ModelForm):
    class Meta:
        model=models.Receiver
        fields="__all__"

class ComplaintForms(forms.ModelForm):
    class Meta:
        model=models.Complaint
        fields="__all__"
