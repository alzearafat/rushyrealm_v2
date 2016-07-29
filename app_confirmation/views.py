import datetime
from django.utils import timezone
from django.template import Context
from .forms import ConfirmationForm
from app_confirmation.models import Confirmation
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string, get_template
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def confirmation_form(request):
    if request.method == "POST":
        form = ConfirmationForm(request.POST, request.FILES)
        if form.is_valid():
            confirmation = form.save(commit=False)
            confirmation.tanggal_konfirmasi = datetime.datetime.now()
            confirmation.save()
            subject = "[RUSHYREALM] ADA YANG KONFIRMASI BREE"
            to = ['alzea.arafat@gmail.com', 'cahyosumirat93@gmail.com']
            from_email = 'hello@rushyrealm.com'
            ctx = {
                'nama': confirmation.nama,
                'id_order': confirmation.id_order,
                'jumlah_transfer': confirmation.jumlah_transfer,
                'tanggal_transfer': confirmation.tanggal_transfer,
                'tanggal_konfirmasi': confirmation.tanggal_konfirmasi,
            }
            message = get_template('email/confirmation_email.html').render(Context(ctx))
            msg = EmailMessage(subject, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()
            return render(request, 'app_confirmation/confirmation_success.html')
    else:
        form = ConfirmationForm()
    return render(request, 'app_confirmation/confirmation_form.html', {'form': form})

def confirmation_success(request):
    return render(request, 'app_confirmation/confirmation_success.html')

def confirmation_login(request):
    if request.user.is_authenticated():
        return redirect('/products/')
    else:
        return render(request, 'app_confirmation/confirmation_login.html')
