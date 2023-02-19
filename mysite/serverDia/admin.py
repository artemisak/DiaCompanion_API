from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import Group

from .models import DiaUsers


# Register your models here.

admin.site.register(DiaUsers, UserAdmin)
admin.site.unregister(Group)