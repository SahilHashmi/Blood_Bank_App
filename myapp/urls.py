from multiprocessing.spawn import import_main_path
from django.urls import path
from . import views

urlpatterns =[
    path('home',views.home,name='home'),
    path('addBB',views.AddBloodBank.as_view(),name="addBB"),
    path('showBBlist',views.showList,name="showBBlist"),
    path('addDO',views.AddDonor.as_view(),name="addDO"),
    path('ListsDonors',views.donorList,name="ListsDonors"),
    path('addRE',views.AddReceiver.as_view(),name="addRE"),
    path('ListsReceivers',views.receiverList,name="ListsReceivers"),
    path('updbb/<id>',views.UpdateBloodBank.as_view(),name="updbb"),
    path('delbb/<id>',views.DeleteBloodBank.as_view(),name="delbb"),
    path('updonor/<id>',views.UpdateDonor.as_view(),name="updonor"),
    path('deldonor/<id>',views.DeleteDonor.as_view(),name="deldonor"),
    path('upreceiver/<id>',views.UpdateReceiver.as_view(),name="upreceiver"),
    path('delreceiver/<id>',views.DeleteReceiver.as_view(),name="delreceiver"),
    path('search',views.Search.as_view(),name='search'),
    path('login',views.Logins.as_view(),name="login"),
    path('logout',views.logouts,name="logout"),
    path('register',views.Registration.as_view(),name="register"),
    path('addCO',views.AddComplaint.as_view(),name="addCO"),
    path('ListsComplaints',views.complaintList,name="ListsComplaints"),
]