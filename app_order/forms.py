from django import forms
from app_order.models import Order
from crispy_forms.helper import FormHelper

class OrderForm(forms.ModelForm):
	class Meta:
		model 	= Order
		fields 	= ['kode_barang', 'ukuran', 'nama', 'email', 'no_tlp', 'alamat',]
		exclude = ['id', 'no_resi', 'tanggal_order']
		widgets = {id : forms.HiddenInput()}