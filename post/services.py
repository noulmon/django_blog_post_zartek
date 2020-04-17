from rest_framework import status
from rest_framework.response import Response

from post.models import Post
from post.serializers import LikedUsersSerializer


class PostServices:
    def like_service(self, post_id, user):
        # checking whether the post exists
        if Post.objects.filter(id=post_id).exists():
            # post object
            post = Post.objects.get(id=post_id)
            # checking whether the post already liked by user
            if post.votes.exists(user.id):
                # unlike post the post if already liked by user
                post.votes.delete(user.id)
                return Response({
                    'return': True,
                    'message': f'{user.username} successfully un-liked the post'
                },
                    status=status.HTTP_200_OK
                )
            # like the post
            post.votes.up(user.id)
            return Response({
                'return': True,
                'message': f'{user.username} successfully liked the post'
            },
                status=status.HTTP_200_OK
            )
        return Response({
            'return': False,
            'message': f'No posts with id: {post_id} found'
        },
            status=status.HTTP_404_NOT_FOUND
        )

    def liked_user_service(self, post_id):
        if Post.objects.filter(id=post_id).exists():
            post = Post.objects.get(id=post_id)
            post_like_data = post.votes.user_ids()
            serializer = LikedUsersSerializer(post_like_data, many=True)
            data = serializer.data
            if len(data) > 0:
                return Response({
                    'return': True,
                    'message': f'Successfully fetched the users who like the post: {post_id}',
                    'data': data,
                })
            return Response({
                'return': True,
                'message': f'The post with id: {post_id} has no likes',
                'data': data,
            })
        return Response({
            'return': False,
            'message': f'No posts with id: {post_id} found'
        },
            status=status.HTTP_404_NOT_FOUND
        )
