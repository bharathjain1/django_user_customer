from django.contrib import admin
from . models import user,customer



# Register your models here.
admin.site.register(user)
admin.site.register(customer)
class UsserAdmin(admin.ModelAdmin):
    list_display=['First_Name','Last_Name','Email_Id','Mobile_No']

class CustomerAdmin(admin.ModelAdmin):
    lis_display=['user','profile_no']
