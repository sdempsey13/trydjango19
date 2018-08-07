from django.urls import path
from posts.views import (
    posts_create,
    posts_detail,
    posts_list,
    posts_update,
    posts_delete,
    )

urlpatterns = [
    path('create', posts_create,),
    path('<int:id>/', posts_detail, name='detail'),
    path('list', posts_list,),
    path('update', posts_update,),
    path('delete', posts_delete,),
]
