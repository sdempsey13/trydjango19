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
    path('', posts_list, name='list'),
    path('<int:id>/edit/', posts_update, name='update'),
    path('<int:id>/delete/', posts_delete,),
]
