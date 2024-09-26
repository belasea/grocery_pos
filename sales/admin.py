from django.contrib import admin
from .models import Sales, salesItems

class SalesAdmin(admin.ModelAdmin):
    list_display = ('code', 'sub_total', 'grand_total', 'tax_amount', 'tax', 'tendered_amount', 'amount_change', 'date_added', 'date_updated')
    search_fields = ('code',)
    list_filter = ('date_added', 'date_updated')
    readonly_fields = ('date_added', 'date_updated')

class SalesItemsAdmin(admin.ModelAdmin):
    list_display = ('sale_id', 'product_id', 'price', 'qty', 'total')
    search_fields = ('sale_id__code', 'product_id__name')
    list_filter = ('sale_id', 'product_id')

admin.site.register(Sales, SalesAdmin)
admin.site.register(salesItems, SalesItemsAdmin)
