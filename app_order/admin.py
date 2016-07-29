from django.contrib import admin
from app_order.models import Order

class OrderAdmin(admin.ModelAdmin):
  model 		= Order
  list_display 	= ('id', 'kode_barang', 'ukuran', 'nama', 'email', 'no_tlp', 'no_resi', 'tanggal_order', 'lunas', 'terkirim')
  list_filter 	= ('tanggal_order', 'lunas', 'terkirim', 'ukuran')
  search_fields = ['id', 'email']

admin.site.register(Order, OrderAdmin)
