from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.my_form, name="my_form")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

