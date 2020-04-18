from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from post.views import PostViewSet, PostAdminViewSet

""" route to view all the posts """
post_list = PostViewSet.as_view({
    'get': 'all',
})

""" route to like/unlike a post """
like_post = PostViewSet.as_view({
    'get': 'like',
})

""" route to get the list of users liked a post (admin only) """
liked_users = PostAdminViewSet.as_view({
    'get': 'liked_users',
})

urlpatterns = format_suffix_patterns([
    path('all/', post_list),
    path('like/<int:pk>/', like_post),
    path('liked_users/<int:pk>/', liked_users),
])
