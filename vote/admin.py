from django.contrib import admin
from .models import Address, Party, UserProfile, State


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(State)
admin.site.register(Party)
