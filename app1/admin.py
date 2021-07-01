from django.contrib import admin
from .models import Compny_Details,Compny_Customers,Compny_Products, Customer_Feedback, Customer_Order
# Register your models here.
admin.site.register(Compny_Details)
admin.site.register(Compny_Customers)
admin.site.register(Compny_Products)
admin.site.register(Customer_Order)
admin.site.register(Customer_Feedback)

