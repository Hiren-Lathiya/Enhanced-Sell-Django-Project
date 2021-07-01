from os import name
from django.urls import path
#from app1.views import registration,login
from .views import *
#from .views import views as v

urlpatterns = [
    path('',login,name='ln'),
    path('registration/',registration,name='rg'),
    path('forgetpass/',ForgetPassword,name='fp'),
    path('logout/',logout,name='logout'),
    path('check_otp/',OTP_Checker,name='co'),
    path('newpassword/',new_password,name='np'),
    path('manageprofile/',Manage_Profile,name='mp'),
    path('add_customers/',AddCustomer,name='addcust'),
    path('view_customers/',ViewCustomer,name='viewcust'),
    path('view_orders/',ViewOrder,name='vieworder'),
    path('feedback/',ViewFeedback,name='feedback'),
    path('acceptorder/<int:id>',AcceptOrder,name='acceptorder'),
    path('denayorder/<int:id>',DenayOrder,name='denayorder'),
    path('del_customres/<int:id>',DeleteCustomer,name='delcust'),
    path('dashboard/',Dashboard,name='db'),
    
    #--------customers------------
    path('custlogin/',Cust_Login,name='custlogin'),
    path('custdash/',Cust_Dashboard,name='custdash'),
    path('custlogout/',Cust_Logout,name='custlogout'),
    path('custprofile/',Cust_Profile,name='custprofile'),
    path('place_order/<int:id>',Place_Order,name='place_order'),
    path('allorders',All_Orders,name='allorder'),
    path('about/',AboutUs,name='about'),
    path("contact/",ContactUs,name='contact'),
    
    
    #___________products_________
    path('addproduct',AddProduct,name='addproduct'),
    path('viewproduct',ViewProduct,name='viewproduct'),
    path('updateproduct/<int:id>',UpdateProduct,name='updateproduct'),
    path('deleteproduct/<int:id>',DeleteProduct,name='deleteproduct'),
]