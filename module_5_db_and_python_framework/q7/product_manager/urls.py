from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',dashboard_view,name='dashboard_view'),
    path('search_view/',search_view,name='search_view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
