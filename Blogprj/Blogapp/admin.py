from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    #list_filter = ['status']




admin.site.register(Task, TaskAdmin)
admin.site.site_header ='Todo App'
admin.site.site_title ='BIBLE EXPOSITORIES'