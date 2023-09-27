from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_verified', 'is_blind', 'is_mute', 'is_deaf', 'password')

# Register the User model with the UserAdmin class
admin.site.register(User, UserAdmin)