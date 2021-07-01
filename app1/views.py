from os import name
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from app1.models import Compny_Details,Compny_Customers, Compny_Products, Customer_Feedback, Customer_Order
import smtplib
import random
import email.message
from django.contrib import messages
# Create your views here.

#------------------compny------------
def registration(request):
    if request.POST:
        nm=request.POST['name']
        em=request.POST['email']
        pass1=request.POST['pass']
        pass2=request.POST['re_pass']
        try:
            car=Compny_Details.objects.get(email=em)
            messages.error(request,'Email alredy registered')
            #return HttpResponse("<h1><a href=''>email alredy registered</a> </h1>")
        except:
             if pass1==pass2:
                 obj=Compny_Details()
                 obj.name=nm
                 obj.email=em
                 obj.password=pass1 #or pass2
                 obj.save()
                 messages.info(request,'Account Created Succesfully!!')
                 return redirect('ln')
             else:
                 messages.error(request,'Both Password Must Be Same!!')
    return render(request,"compny/login/registration.html")


def login(request): 
    if request.POST:
      em=request.POST['email']
      passd = request.POST['pass']
      #print(em,passd)
      
      try:
           var=Compny_Details.objects.get(email=em)
           #print(var)
           if var.password==passd:
               request.session['comp_data']=var.id
               messages.info(request,'Login Succesfully!!')
               return redirect('db')
               
           else:
                messages.error(request,'Wrong Password!!!')
                return redirect('ln')
                #return HttpResponse("<h1><a href=''>wrong password</a> </h1>")
      except:
          messages.error(request,'Email Not Registered')
          return redirect('ln')
          #return HttpResponse("<h1><a href=''>email not registered</a> </h1>")
    return render(request,"compny/login/login.html")

   
def logout(request):
        if 'comp_data' in request.session.keys():
            del request.session['comp_data']
            messages.info(request,'Logged Out Success')
            return redirect('ln')
        else:
             return redirect('ln')
         
         
def ForgetPassword(request):
    if request.POST:
        em1 = request.POST['em']
        try:
            valid = Compny_Details.objects.get(email = em1)
            #print(valid)
            
            sender_email = "hdroyal1142@gmail.com"
            sender_pass = '8320903816h'
            reciv_email = em1      
            
            server = smtplib.SMTP('smtp.gmail.com',587)
            
            # OTP Create---------
            nos = [1,2,3,4,5,6,7,8,9,0]
            otp = ""
            for i in range(6):
                otp += str(random.choice(nos))
            #print(otp)
            
            mes1 = f"""
            This Is Your OTP From This New Site
            {otp}
            
            
            Note:- Don't share With Others......
            """
            
            msg = email.message.Message()
            msg['Subject'] = "OTP For reset password"
            msg['From'] = sender_email
            msg['To'] = reciv_email
            password = sender_pass
            msg.add_header('Content-Type','text/html')
            msg.set_payload(mes1)
            
            server.starttls()
            server.login(msg['From'],password)
            server.sendmail(msg['From'],msg['To'],msg.as_string())
            
            request.session['otp'] = otp
            request.session['New_User'] = valid.id  
            
            #print(request.session['New_User'])
            #print(request.session['otp'])
            messages.info(request,'OTP Send Successfully')
            return redirect('co')
        except:
            messages.error(request,' You Have Entered Wrong Email Id')
            #return HttpResponse("<a href=''> You Have Entered Wrong Email Id </a>")
    return render(request,'compny/login/forgetpass.html')


def OTP_Checker(request):
    if 'otp' in request.session.keys():
        if request.POST:
            otp1=request.POST['otp']
            #print(otp1)
            #print(request.session['otp'])
            if request.session['otp']==otp1:
                del request.session['otp']
                return redirect('np')
            else:
                messages.error(request,' You Have Entered Wrong OTP')
                del request.session['otp']
                return redirect('fp')
        return render (request,'compny/login/otp_check.html')
    else:
        return redirect('ln')
    

def new_password(request):
    if 'New_User' in request.session.keys():
        if request.POST:
            p1=request.POST['pass1']
            p2=request.POST['pass2']
            #print(p1,p2)
            if p1==p2:
                obj=Compny_Details.objects.get(id=int(request.session['New_User']))
                obj.password=p1 #or p2
                obj.save()
                del request.session['New_User']
                messages.info(request,'Password Updated Successfully')
                return redirect('ln')               
            else:
                messages.error(request,'Both Password Must Be Same')
                #return HttpResponse("<h1><a href=''>Both passwords are not same</a> </h1>")

                
        return render (request,'compny/login/newpassword.html')
    else:
        return redirect('fp')
    
    
def Dashboard(request):
    if 'comp_data' in request.session.keys():
       comp=Compny_Details.objects.get(id=int(request.session['comp_data']))
       ord=Customer_Order.objects.filter(comp=comp)
       return render(request,"compny/dashboard/dashboard.html",{'USERS':comp,'ord':ord})
    else:
        return redirect('ln')
    
def Manage_Profile(request):
    if 'comp_data' in request.session.keys():
        comp=Compny_Details.objects.get(id=int(request.session['comp_data']))
        if request.POST:
            nm=request.POST['nm1']
            em=request.POST['em1']
            con=request.POST['con1']
            add=request.POST['add1']
            pas=request.POST['pass1']
            img=request.FILES.get('img1')
            
            comp.name=nm
            comp.email=em
            comp.number=con
            comp.address=add
            comp.password=pas
            #print(img)
            if img!=None:
               comp.profile=img
            messages.info(request,'Profile Updated Succesfully!!')
            comp.save()
            #return redirect('db')
            
        return render(request,"compny/dashboard/profile.html",{'USERS':comp})
    else:
        return redirect('ln')
    
   
def AddCustomer(request):
    if 'comp_data' in request.session.keys():
       comp=Compny_Details.objects.get(id=int(request.session['comp_data']))
       if request.POST:
           nm=request.POST['nm1']
           em=request.POST['em1']
           con=request.POST['con1']
           
           obj=Compny_Customers()
           obj.comp=comp
           obj.custName=nm
           obj.custMail=em
           obj.custCon=con
           
           #---------------Password Creation------------
           Lalpha='poiuytrewqlkjhgfdsamnbvcxz'
           Ualpha='POIUYTREWQLKJHGFDSAMNBVCX'
           spechar='!@#$%^&*()'
           num='1234567890'
           data=Lalpha+Ualpha+spechar+num
           pswd = ""
           for i in range(8):
                    pswd += str(random.choice(data))
           #print(pswd)
            
           mes1 = f"""
                    hello this is your new login id and password
                    link:http://localhost:8000/custlogin
                    email id={em}
                    Password={pswd}           
            
                    Note:- Don't share With Others......
                    """
           obj.custPass=pswd
           messages.info(request,'Customer Added Succesfully!!')
           obj.save()
           try:
                sender_email = "hdroyal1142@gmail.com"
                sender_pass = '8320903816h'
                reciv_email = em      
            
                server = smtplib.SMTP('smtp.gmail.com',587)
    
                msg = email.message.Message()
                msg['Subject'] = "New Customer Added"
                msg['From'] = sender_email
                msg['To'] = reciv_email
                password = sender_pass
                msg.add_header('Content-Type','text/html')
                msg.set_payload(mes1)
            
                server.starttls()
                server.login(msg['From'],password)
                server.sendmail(msg['From'],msg['To'],msg.as_string())
                return redirect('viewcust')
           except:
               messages.error(request,'Unexpected Error Occured,Try After Sometimes !!')
                    #return HttpResponse("<a href=''> error occurs</a>")  
       return render(request,"compny/dashboard/add_customers.html",{'USERS':comp})
    else:
        return redirect('ln')
    
def ViewCustomer(request):
     if 'comp_data' in request.session.keys():
       comp_user=Compny_Details.objects.get(id=int(request.session['comp_data']))
       cust=Compny_Customers.objects.filter(comp=comp_user)
       #cust=Compny_Customers.objects.all(comp)
       #print(cust)
       #messages.info(request,'Customer Added Succesfully!!')
       return render(request,"compny/dashboard/view_customers.html",{'USERS':comp_user,'cust':cust})
     else:
          return redirect('ln')

def ViewFeedback(request):
    if 'comp_data' in request.session.keys():
       comp_user=Compny_Details.objects.get(id=int(request.session['comp_data']))
       cust=Compny_Customers.objects.filter(comp=comp_user)
       fb=Customer_Feedback.objects.all()
       #cust=Compny_Customers.objects.all(comp)
       #print(cust)
       return render(request,"compny/dashboard/feedback.html",{'fb':fb,'cust':cust,'USERs':comp_user})
    else:
          return redirect('ln')

    

def DeleteCustomer(request,id):
     if 'comp_data' in request.session.keys():
       cust=Compny_Customers.objects.get(id=id)
       cust.delete()
       messages.error(request,'Customer Deleted Successfully!!')
       return redirect('viewcust')
     else:
          return redirect('ln')
         
def AddProduct(request):
    if 'comp_data' in request.session.keys():
       comp=Compny_Details.objects.get(id=int(request.session['comp_data']))
       if request.POST:
           nm=request.POST['nm1']
           prc=request.POST['prc1']
           qty=request.POST['qt1']
           img=request.FILES.get('img1')
        
           obj=Compny_Products()
           obj.comp=comp   #first comp is field of cut product and secnd comp is variable defined above
           obj.proName=nm
           obj.proPrice=prc
           obj.proQnty=qty
           obj.proImg=img
           obj.save()
           messages.info(request,'Product Added Succesfully!!')
           return redirect('viewproduct')
              
       return render(request,"compny/dashboard/add_products.html",{'USERS':comp})
    else:
        return redirect('ln')

def UpdateProduct(request,id):
    if 'comp_data' in request.session.keys():
       comp=Compny_Details.objects.get(id=int(request.session['comp_data']))
       prod=Compny_Products.objects.get(id=id)
       if request.POST:
           nm=request.POST['nm1']
           prc=request.POST['prc1']
           qty=request.POST['qt1']
           img=request.FILES.get('img1')
        
          
           prod.comp=comp   #first comp is field of cut product and secnd comp is variable defined above
           prod.proName=nm
           prod.proPrice=prc
           prod.proQnty=qty
           if img!=None:
              prod.proImg=img
           messages.info(request,'Product Updated Succesfully!!')
           prod.save()
           return redirect('viewproduct')
       return render(request,"compny/dashboard/update_products.html",{'USERS':comp,'prod':prod})
    else:
        return redirect('ln')

def ViewProduct(request):
    if 'comp_data' in request.session.keys():
       comp_user=Compny_Details.objects.get(id=int(request.session['comp_data']))
       prod=Compny_Products.objects.filter(comp=comp_user)
       return render(request,"compny/dashboard/view_products.html",{'USERS':comp_user,'prod':prod})
    else:
        return redirect('ln')
    
def DeleteProduct(request,id):
    if 'comp_data' in request.session.keys():
        prod=Compny_Products.objects.get(id=id)
        prod.delete()   
        messages.error(request,'Product Deleted Successfully!!') 
        return redirect('viewproduct')
    else:
        return redirect('ln')

def ViewOrder(request):
    if 'comp_data' in request.session.keys():
       comp=Compny_Details.objects.get(id=int(request.session['comp_data']))
       cordr=Customer_Order.objects.filter(comp=comp,status='False') 
       #first comp is defined above and second comp is field of Customer_order model
       return render(request,"compny/dashboard/vieworders.html",{'USERS':comp,'cordr':cordr})
    else:
        return redirect('ln')

def AcceptOrder(request,id):
    if 'comp_data' in request.session.keys():
       cordr=Customer_Order.objects.get(id=id) 
       cordr.status='Yes'
       cordr.save()
       #first comp is defined above and second comp is field of Customer_order model
       return redirect('vieworder')
    else:
        return redirect('ln')

        
def DenayOrder(request,id):
    if 'comp_data' in request.session.keys():
       cordr=Customer_Order.objects.get(id=id) 
       cordr.status='No'
       cordr.save()
       #first comp is defined above and second comp is field of Customer_order model
       return redirect('vieworder')
    else:
        return redirect('ln')

#--------------------Customer---------------

def Cust_Login(request):
    if request.POST:
        em=request.POST['em1']
        pps=request.POST['pass1']
        try:
            valid=Compny_Customers.objects.get(custMail=em,custPass=pps)
            request.session['custmer_users']=valid.id
            messages.info(request,"Login Successfully")
            return redirect('custdash')
        except:
            messages.error(request,"Invelid Credentials")
            return redirect('custlogin')
        
    return render (request,"customers/login/login.html")

def Cust_Dashboard(request):
    if 'custmer_users' in request.session.keys():
       cust=Compny_Customers.objects.get(id=int(request.session['custmer_users']))
       prod=Compny_Products.objects.filter(comp=cust.comp)
       
       return render (request,'customers/dashboard/index.html',{'prod':prod})
    else:
        return redirect('custlogin')

def Cust_Logout(request):
    if 'custmer_users' in request.session.keys():
            del request.session['custmer_users']
            messages.info(request,"Logout Successfully")           
            return redirect('custlogin')
    else:
             return redirect('custlogin')


def Place_Order(request,id):
    if 'custmer_users' in request.session.keys():
       cust=Compny_Customers.objects.get(id=int(request.session['custmer_users']))
       prod=Compny_Products.objects.get(id=id)
       if request.POST:
           qty1=request.POST['qty1']
           obj=Customer_Order()
           obj.comp=prod.comp
           obj.cust=cust
           obj.prod=prod
           obj.qty=qty1
           obj.status='False'
           obj.total_price= int( int(qty1) * int(prod.proPrice) )
           messages.info(request,"Order Placed Successfully")
           obj.save()
           return redirect('allorder')
       
       return render (request,'customers/dashboard/place_order.html',{'prod':prod})
    else:
        return redirect('custlogin')
   
def AboutUs(request):
    if 'custmer_users' in request.session.keys():
       return render (request,'customers/dashboard/about.html')
    else:
        return redirect('custlogin')

def ContactUs(request):
    if 'custmer_users' in request.session.keys():
       cust=Compny_Customers.objects.get(id=int(request.session['custmer_users']))
       if request.POST:
           em1=request.POST['em']
           sub=request.POST['sub1']
           msg=request.POST['msg1']
           obj=Customer_Feedback()
           obj.name=cust.custName
           obj.mail=em1
           obj.subject=sub
           obj.message=msg
           messages.info(request,"Form Submited Successfully")
           obj.save()
           return redirect('custdash')
       return render (request,'customers/dashboard/contact.html',{'cust':cust})
    else:
        return redirect('custlogin')
    
def All_Orders(request):
    if 'custmer_users' in request.session.keys():
       cust=Compny_Customers.objects.get(id=int(request.session['custmer_users']))
       ord=Customer_Order.objects.filter(cust=cust)       
       return render (request,'customers/dashboard/all_order.html',{'ord':ord})
    else:
        return redirect('custlogin')
        
def Cust_Profile(request):
     if 'custmer_users' in request.session.keys():
       cust=Compny_Customers.objects.get(id=int(request.session['custmer_users'])) 
       if request.POST:
           nm=request.POST['nm1']
           em=request.POST['em1']
           ps=request.POST['ps1']
           cn=request.POST['cn1']
           ad=request.POST['ad1']
           im=request.FILES.get('img1')
           
           cust.custName=nm
           cust.custMail=em
           cust.custPass=ps
           cust.custCon=cn
           cust.custAdd=ad
           if im != None:
               cust.custProfile=im
           messages.info(request,' Profile Updated Succesfully ,All Changes Are been Saved')
           cust.save()
           return redirect('custprofile')
       return render (request,'customers/dashboard/profile.html',{'cust':cust})
     else:
        return redirect('custlogin')