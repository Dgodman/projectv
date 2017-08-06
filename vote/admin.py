from django.contrib import admin
from .models import Address, Party, UserProfile, State


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name_short', 'absentee_type',)
    fields = ('name_short', 'absentee_type', )
    list_filter = ('absentee_type', )


admin.site.register(Party)
