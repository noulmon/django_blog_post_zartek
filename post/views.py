from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from post.services import PostServices

post_services = PostServices()


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=True, url_name='posts_list', )
    def all(self, request):
        """
        :param request: user request
        :return: list of posts ordered by the tags most liked by the user
        """
        user = request.user
        return post_services.list_services(user=user)

    def like(self, request, pk):
        """
        :param request: user request
        :param pk: post id
        :return: whether the user have liked/un-liked the post
        """
        user = request.user
        """ checking whether the user is admin or not(admin users are not allowed to like the post) """
        if not user.is_staff:
            return post_services.like_service(post_id=pk, user=user)
        return Response({
            'return': False,
            'message': 'Admin user is not permitted to like/unlike post',
        },
            status=status.HTTP_403_FORBIDDEN
        )


class PostAdminViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]

    def liked_users(self, request, pk):
        """
        :param request: user request
        :param pk: post id
        :return: list of all users who have liked a post
        """
        return post_services.liked_user_service(post_id=pk)
