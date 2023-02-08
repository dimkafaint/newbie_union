from django.urls import path

from .views import (index, group_blog, post_edit, profile,
                    post_detail, post_create, add_comment,
                    follow_index, profile_follow, profile_unfollow)

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('group/<slug:slug>/', group_blog, name='group_list'),
    path('profile/<str:username>/', profile, name='profile'),
    path('create/', post_create, name='post_create'),
    path('blog/<int:post_id>/edit/', post_edit, name='post_edit'),
    path('blog/<int:post_id>/', post_detail, name='post_detail'),
    path('blog/<int:post_id>/comment/', add_comment, name='add_comment'),
    path('follow/', follow_index, name='follow_index'),
    path('profile/<str:username>/follow/',
         profile_follow,
         name='profile_follow'),
    path('profile/<str:username>/unfollow/',
         profile_unfollow,
         name="profile_unfollow"),
]
