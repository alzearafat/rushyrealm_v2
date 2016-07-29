import datetime
from .forms import OrderForm
from django.utils import timezone
from app_order.models import Order
from django.template import Context
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def order_form(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.tanggal_order = datetime.datetime.now()
            order.save()
            subject = "[RUSHYREALM] NEW ORDER!"
            to = [order.email, 'alzea.arafat@gmail.com', 'cahyosumirat93@gmail.com']
            from_email = 'hello@rushyrealm.com'
            ctx = {
                'nama': order.nama,
                'kode_barang': order.kode_barang,
                'id_order': order.id,
            }
            message = get_template('email/order_email.html').render(Context(ctx))
            msg = EmailMessage(subject, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()
            return render(request, 'app_order/order_success.html')
    else:
        form = OrderForm()
    return render(request, 'app_order/order_form.html', {'form': form})

def order_success(request):
    return render(request, 'app_order/order_success.html')

def order_login(request):
    if request.user.is_authenticated():
        return redirect('/products/')
    else:
        return render(request, 'app_order/order_login.html')
