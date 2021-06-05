from django.contrib import admin

from .models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created','updated']
    list_filter = ['available', 'created', 'updated']   #過濾器
    list_editable = ['price', 'stock', 'available']     #直接由admin首頁編輯
    prepopulated_fields = {'slug': ('name',)}   #根據name自動生成slug

admin.site.register(Product,ProductAdmin)
# Register your models here.
