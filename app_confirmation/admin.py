from django.contrib import admin
from app_confirmation.models import Confirmation

class ConfirmationAdmin(admin.ModelAdmin):
  model 		= Confirmation
  list_display 	= ('id_order', 'tanggal_transfer', 'nama', 'jumlah_transfer','tanggal_konfirmasi',)
  list_filter 	= ('tanggal_transfer', 'tanggal_konfirmasi',)
  search_fields = ['id_order', 'nama']

admin.site.register(Confirmation, ConfirmationAdmin)