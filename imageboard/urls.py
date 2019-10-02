from django.urls import path , include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('image/', image , name='image'),
    path('image/detail/<int:image_id>/', image_detail, name = 'image_detail'),
    path('image/post/', ImagePost.as_view() , name = 'image_post'),
    path('image/edit/<int:image_detail_id>/' , image_edit , name = 'image_edit'),
    path('image/delete/<slug:pk>/', ImageDelete.as_view() , name = 'image_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
