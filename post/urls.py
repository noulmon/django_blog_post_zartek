from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from post.views import PostViewSet, PostAdminViewSet
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'posts', PostViewSet, basename='post')
# urlpatterns = router.urls

post_list = PostViewSet.as_view({
    'get': 'all',
})

like_post = PostViewSet.as_view({
    'get': 'like',
})

liked_users = PostAdminViewSet.as_view({
    'get': 'liked_users',
})

urlpatterns = format_suffix_patterns([
    path('all/', post_list),
    path('like/<int:pk>/', like_post),
    path('liked_users/<int:pk>/', liked_users),
])
