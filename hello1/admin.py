from django.contrib import admin
from .models import User,Product

# Register your models here.
# For showing user information on admin panel

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','mobile','address']
    
    
# This model will show product fields on admin panel    
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','name','auth_name','price','description','image']