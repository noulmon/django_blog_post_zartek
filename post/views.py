from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from post.models import Post
from post.serializers import PostSerializer, LikedUsersSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

from post.services import PostServices

post_service = PostServices()


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=True, url_name='posts_list', description='hello')
    def all(self, request):
        queryset = Post.objects.all()
        user = request.user
        serializer = PostSerializer(queryset, context={'user': user}, many=True)
        return Response({
            'return': True,
            'message': 'Post list fetched successfully',
            'posts': serializer.data
        },
            status=status.HTTP_200_OK
        )

    def like(self, request, pk):
        user = request.user
        # checking whether the user is admin or not(admin users are not allowed to like the post)
        if not user.is_staff:
            return post_service.like_service(post_id=pk, user=user)
        return Response({
            'return': False,
            'message': 'Admin user is not permitted to like/unlike post',
        },
            status=status.HTTP_403_FORBIDDEN
        )


class PostAdminViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]

    def liked_users(self, request, pk):
        return post_service.liked_user_service(post_id=pk)
