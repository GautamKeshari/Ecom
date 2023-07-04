from django.contrib import admin
from .models import Products,Order

# Register your models here.
admin.site.site_header="E-com Online Shopping"
admin.site.site_title="Online Shopping"
admin.site.index_title="Manage User's Data"

class ProductFullData(admin.ModelAdmin):

    # for changing action in admin panel
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    
    change_category_to_default.short_description='Default Category'
    # change name of "change_category_to_default"  to "Default category"
    list_display=('title','price','discounted_price','category','description')
    search_fields=('title','category')
    actions=('change_category_to_default',)
    # for hiding certain fields
    fields=('title','description','image')
    list_editable=('title','category')
    list_display_links=None

admin.site.register(Products,ProductFullData)
# admin.site.register(ProductFullData)  We don't write above line like this.
admin.site.register(Order)