from django.urls import path , include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
# from ckeditor_uploader import urls
from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views as views_ckeditor
from django.views.decorators.cache import never_cache

urlpatterns = [
    # =================================notice=======================================
    path('notice/', notice , name='notice'),
    path('notice/detail/<slug:pk>/', NoticeDetail.as_view() , name = 'notice_detail'),
    path('notice/post/', NoticePost.as_view() , name = 'notice_post'),
    path('notice/edit/<int:notice_detail_id>/' , notice_edit , name = 'notice_edit'),
    path('notice/delete/<slug:pk>/', NoticeDelete.as_view() , name = 'notice_delete'),
    # ==============================================================================

    # ===============================ckeditor=======================================
    path('upload/', login_required(views_ckeditor.upload), name='ckeditor_upload'),
    path('browse/', never_cache(login_required(views_ckeditor.browse)), name='ckeditor_browse'),
    # ==============================================================================
    
    # =================================free=========================================
    path('free/', free , name='free'),
    path('free/detail/<slug:pk>/', FreeDetail.as_view() , name = 'free_detail'),
    path('free/post/', FreePost.as_view() , name = 'free_post'),
    path('free/edit/<int:free_detail_id>/' , free_edit , name = 'free_edit'),
    path('free/delete/<slug:pk>/', FreeDelete.as_view() , name = 'free_delete'),
    # ==============================================================================

    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
