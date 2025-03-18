from django.contrib import admin
from django.urls import path, include
from .views import home
from mywebsite.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)
