from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.views import View
from . import forms,models
from django.contrib.auth import logout

# Create your views here.

def home(request):
    return render(request,'home.html')

class Logins(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        unm=request.POST['unm']
        passs=request.POST['pass']
        data=models.MyUser.objects.filter(username__iexact=unm).filter(password__iexact=passs)
        if data:
            for dt in data:
                request.session['utype']=dt.usertype
                request.session['username']=dt.firstname+""+dt.lastname

            return redirect('home')
        else:
            return HttpResponse("<h3>Invalid Credentials......")

def logouts(request):
    logout(request)
    return redirect('login')

class Registration(View):
    def get(self,request):
        myforms=forms.MyUserForm()
        return render(request,'register.html',{'myforms':myforms})
    def post(self,request):
        myforms=forms.MyUserForm(request.POST)
        if myforms.is_valid():
            myforms.save()
            return redirect('login')
        else:
            return HttpResponse("<h3>Invalid Data")

class AddBloodBank(View):
    def get(self,request):
        myforms=forms.BloodBankForms()
        return render(request,'addBank.html',{'myforms':myforms})

    def post(self,request):
        myforms=forms.BloodBankForms(request.POST)
        if myforms.is_valid():
            myforms.save()
            return redirect('home')

def showList(request):
    data=models.Bloodbank.objects.all().order_by('bloodbankid')
    return render(request,'showBBlist.html',{'data':data})


class UpdateBloodBank(View):
    def get(self,request,id):
        obj=get_object_or_404(models.Bloodbank,bloodbankid=id)
        myforms=forms.BloodBankForms(instance=obj)
        return render(request,'updbb.html',{'myforms':myforms})
    def post(self,request,id):
        obj=get_object_or_404(models.Bloodbank,bloodbankid=id)
        myforms=forms.BloodBankForms(request.POST,instance=obj)
        if myforms.is_valid():
            myforms.save()
            return redirect('showBBlist')

class DeleteBloodBank(View):
    def get(self,request,id):
        obj=get_object_or_404(models.Bloodbank,bloodbankid=id)
        myforms=forms.BloodBankForms(instance=obj)
        return render(request,'delbb.html',{'myforms':myforms})

    def post(self,request,id):
        obj=get_object_or_404(models.Bloodbank,bloodbankid=id)
        obj.delete()
        return redirect('showBBlist')

class Search(View):
    def get(self,request):
        return render(request,'search.html')

    def post(self,request):
        bg=request.POST['bg']
        ct=request.POST['ct']
        if(bg and not ct):
            data=models.Donor.objects.filter(bloodgroup__iexact=bg)
        elif(not bg and ct):
            data=models.Donor.objects.filter(city__iexact=ct)
        elif(bg and ct):
            data=models.Donor.objects.filter(bloodgroup__iexact=bg).filter(city__iexact=ct)
        else:
            data=models.Donor.objects.all()
        return render(request,'donorlist.html',{'mydata':data})

# .................Donors................................

class AddDonor(View):
    def get(self,request):
        myforms=forms.DonorForm()
        return render(request,'addDonor.html',{'myforms':myforms})

    def post(self,request):
        myforms=forms.DonorForm(request.POST)
        if myforms.is_valid():
            myforms.save()
            return redirect('home')

def donorList(request):
    data=models.Donor.objects.all().order_by('donorid')
    return render(request,'ListsDonors.html',{'data':data})


#...................Update Donor..........................|
                                                          

class UpdateDonor(View):
    def get(self,request,id):
        obj=get_object_or_404(models.Donor,donorid=id)
        myforms=forms.DonorForm(instance=obj)
        return render(request,'updonor.html',{'myforms':myforms})
    def post(self,request,id):
        obj=get_object_or_404(models.Donor,donorid=id)
        myforms=forms.DonorForm(request.POST,instance=obj)
        if myforms.is_valid():
            myforms.save()
            return redirect('ListsDonors')

#...................Delete Donor..........................


class DeleteDonor(View):
    def get(self,request,id):
        obj=get_object_or_404(models.Donor,donorid=id)
        myforms=forms.DonorForm(instance=obj)
        return render(request,'deldonor.html',{'myforms':myforms})

    def post(self,request,id):
        obj=get_object_or_404(models.Donor,donorid=id)
        obj.delete()
        return redirect('ListsDonors')

#...................Receivers..........................


class AddReceiver(View):
    def get(self,request):
        myforms=forms.ReceiverForms()
        return render(request,'addreceiver.html',{'myforms':myforms})

    def post(self,request):
        myforms=forms.ReceiverForms(request.POST)
        if myforms.is_valid():
            myforms.save()
            return redirect('home')

def receiverList(request):
    data=models.Receiver.objects.all().order_by('receiverid')
    return render(request,'ListsReceivers.html',{'data':data})


#...................Update Receiver..........................
                                                          

class UpdateReceiver(View):
    def get(self,request,id):
        obj=get_object_or_404(models.Receiver,receiverid=id)
        myforms=forms.ReceiverForms(instance=obj)
        return render(request,'upreceiver.html',{'myforms':myforms})
    def post(self,request,id):
        obj=get_object_or_404(models.Receiver,receiverid=id)
        myforms=forms.ReceiverForms(request.POST,instance=obj)
        if myforms.is_valid():
            myforms.save()
            return redirect('ListsReceivers')

#...................Delete Receiver..........................


class DeleteReceiver(View):
    def get(self,request,id):
        obj=get_object_or_404(models.Receiver,receiverid=id)
        myforms=forms.ReceiverForms(instance=obj)
        return render(request,'delreceiver.html',{'myforms':myforms})

    def post(self,request,id):
        obj=get_object_or_404(models.Receiver,receiverid=id)
        obj.delete()
        return redirect('ListsReceivers')

#...................Complaint..........................


class AddComplaint(View):
    def get(self,request):
        myforms=forms.ComplaintForms()
        return render(request,'addcomplaint.html',{'myforms':myforms})

    def post(self,request):
        myforms=forms.ComplaintForms(request.POST)
        if myforms.is_valid():
            myforms.save()
            return redirect('home')

def complaintList(request):
    data=models.Complaint.objects.all()
    return render(request,'ListsComplaints.html',{'data':data})
