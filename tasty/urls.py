from django.urls import path
from . import views

app_name = 'tasty'

urlpatterns = [
    
    path('', views.tastyList, name='tastylist'),
    path('<int:tasty_id>/detail/', views.tastyDetail, name='tastydetail'),
    
    path('<int:tasty_id>/tastycomment/create/', views.tastyCommentCreate, name='tastycommentcreate'),
]