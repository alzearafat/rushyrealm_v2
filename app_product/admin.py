from django.contrib import admin
from app_product.models import Product
from app_product.models import Product_Categories

class ProductAdmin(admin.ModelAdmin):
  model 		= Product
  list_display 	= ('kode', 'nama', 'kategori', 'harga', 'tanggal_publish', 'sale',)
  list_filter 	= ('tanggal_publish', 'kategori', 'sale',)

class Product_CategoriesAdmin(admin.ModelAdmin):
  model 		= Product_Categories
  list_display 	= ('id', 'nama_kategori')

admin.site.register(Product, ProductAdmin)
admin.site.register(Product_Categories, Product_CategoriesAdmin)
