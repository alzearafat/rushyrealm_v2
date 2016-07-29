from . import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.order_form, name='order_form'),
    url(r'^login/$', views.order_login, name='order_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
