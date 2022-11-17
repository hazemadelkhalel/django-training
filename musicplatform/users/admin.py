from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin 
from django import forms

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class AccountsUserAdmin(UserAdmin):
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User,AccountsUserAdmin)