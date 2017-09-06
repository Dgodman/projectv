from django.contrib import admin
from .models import Address, Party, UserProfile, State, StateRule, StateException


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name_long', 'can_vote_by_mail', )
    ordering = ('name_long', )


@admin.register(StateRule)
class StateRuleAdmin(admin.ModelAdmin):
    pass


@admin.register(StateException)
class StateExceptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Party)
