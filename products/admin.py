from django.contrib import admin
from .models import Product, ProductImage, OrderRequest, ProductFormType

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'volume',
        'layers',
        'length',
        'width',
        'height',
        'thickness',
        'price',
        'in_stock',
        'form_type',
    )
    list_filter = ('volume', 'layers', 'form_type', 'in_stock')
    search_fields = ('name',)
    inlines = [ProductImageInline]


@admin.register(OrderRequest)
class OrderRequestAdmin(admin.ModelAdmin):
    def short_message(self, obj):
        return obj.message[:50] + '...' if obj.message and len(obj.message) > 50 else obj.message
    short_message.short_description = "Сообщение"

    list_display = ('name', 'phone', 'email', 'short_message', 'product', 'created_at')
    readonly_fields = ('name', 'phone', 'email', 'message', 'product', 'created_at')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('created_at',)



@admin.register(ProductFormType)
class ProductFormTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)