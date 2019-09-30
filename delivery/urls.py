from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('delivery/', delivery , name='delivery'),
    path('delivery/<int:list_id>', delivery_list, name = 'delivery_list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

