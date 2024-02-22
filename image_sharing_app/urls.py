
# image_sharing_app/urls.py
from django.urls import path
from core import views

urlpatterns = [
    path('', views.image_list, name='image_list'), 
    path('upload', views.image_upload, name='image_upload'),
    path('like/<int:image_id>/$', views.like_image, name='like_image'),
    path('dislike/<int:image_id>/$', views.dislike_image, name='dislike_image'),
]
