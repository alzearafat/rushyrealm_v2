from . import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.confirmation_form, name='confirmation_form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
