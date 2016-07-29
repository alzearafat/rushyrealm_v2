from . import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.product_list_all, name='product_list_all'),
    url(r'^product/(?P<id>[-\w]+)/$', views.product_single, name='product_single'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
