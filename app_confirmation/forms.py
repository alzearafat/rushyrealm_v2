from django import forms
from crispy_forms.helper import FormHelper
from app_confirmation.models import Confirmation

class ConfirmationForm(forms.ModelForm):
	class Meta:
		model 	= Confirmation
		fields 	= ['id_order', 'nama', 'jumlah_transfer', 'tanggal_transfer', 'bukti_transfer']
		exclude = ['tanggal_konfirmasi']
