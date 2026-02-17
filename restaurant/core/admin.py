from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)

@admin.register(Momo)
class MomoAdmin(admin.ModelAdmin):
    list_display =['id','name','decs','price']

