from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'client_name',
        'order_type',
        'status',
        'total_price',
        'remaining',
        'created_at'
    )

    search_fields = (
        'client_name',
        'phone',
        'order_type'
    )

    list_filter = (
        'status',
        'created_at'
    )

    readonly_fields = (
        'remaining',
        'created_at'
    )

    ordering = ('-created_at',)
readonly_fields = (
    'remaining',
)