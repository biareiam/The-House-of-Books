"""Set up of django admin site for profiles app"""
from django.contrib import admin
from checkout.models import Order
from .models import UserProfile, SavedEventList


class OrderAdminInline(admin.TabularInline):
    """
    Order instances to be shown inside the UserProfile.
    Fields are read only, with link to view/edit the full Order
    """
    model = Order
    show_change_link = True
    readonly_fields = (
        'order_number', 'date', 'full_name', 'email', 'grand_total'
        )
    fields = ['date', 'full_name', 'email', 'grand_total']


class SavedEventListAdminInline(admin.TabularInline):
    """
    SavedEventList to be shown inside the UserProfile.
    """
    model = SavedEventList


class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin set up for UserProfile model - show the two inline models
    so user's Orders and SavedEventList are accessible from this view
    """
    inlines = (OrderAdminInline, SavedEventListAdminInline,)


admin.site.register(UserProfile, UserProfileAdmin)