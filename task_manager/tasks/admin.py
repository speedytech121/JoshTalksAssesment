from django.contrib import admin
from .models import User, Task

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile')
    search_fields = ('name', 'email')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'created_at')
    search_fields = ('name',)
    list_filter = ('status',)

admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)
