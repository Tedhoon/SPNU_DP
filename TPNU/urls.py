from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('delivery.urls')),
    path('', include('main.urls')),
    path('', include('board.urls')),
    path('', include('user.urls')),
    path('', include('imageboard.urls')),   
]
