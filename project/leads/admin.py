from django.contrib import admin
from .models import Lead

class LeadAdmin(admin.ModelAdmin):
	list_display = ['name','email','message','created_at']

admin.site.register(Lead, LeadAdmin)
# Register your models here.
