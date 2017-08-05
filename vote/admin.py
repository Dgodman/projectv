from django.contrib import admin
from .models import AddressType, Address, Party, UserProfile


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(AddressType)
admin.site.register(Party)