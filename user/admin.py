from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import employee
# Register your models here.

class employeeInline(admin.StackedInline):
    model = employee
    can_delete = False
    verbose_name_plural = 'employee'

class UserAdmin(UserAdmin):
    inlines = (employeeInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
