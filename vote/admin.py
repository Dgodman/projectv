from django.contrib import admin
# from .models import Address, Party, UserProfile, State, AbsenteeType, AddressType
from .models import Address, Party, UserProfile, State, AbsenteeType


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name_short', 'absentee_type', )
    fields = ('name_short', 'absentee_type', )
    list_filter = ('absentee_type', )


@admin.register(AbsenteeType)
class AbsenteeTypeAdmin(admin.ModelAdmin):
    fields = ('name', 'days_prior', )


admin.site.register(Party)
# admin.site.register(AddressType)
