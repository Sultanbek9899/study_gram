from django.contrib import admin

# Register your models here.
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
    list_editable = ['is_active', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    filter_horizontal = ['followers']