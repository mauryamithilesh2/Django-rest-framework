from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):    #for readonly for profileinterface 
    readonly_fields = ('id',)

admin.site.register(Profile,ProfileAdmin)