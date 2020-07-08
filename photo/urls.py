from django.urls import path

from . import views

app_name = 'photo'

urlpatterns = [
    # photo list
    path('', views.photoList, name='list'),

    # photo detail
    path('<int:photo_id>/detail/', views.photoDetail, name='detail'),

    # 만들자 만들어
    path('upload/', views.photoUpload, name='upload'),

    # post update
    path('<int:photo_id>/update/', views.photoUpdate, name='update'),

    # 삭제인데
    path('<int:photo_id>/delete/', views.photoDelete, name='delete'),
    
]
