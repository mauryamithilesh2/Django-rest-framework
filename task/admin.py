from django.contrib import admin

from .models import Task,Tasklist,Attachment



admin.site.register(Tasklist)
admin.site.register(Task)
admin.site.register(Attachment)
