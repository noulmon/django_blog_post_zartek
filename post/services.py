from itertools import chain

from rest_framework import status
from rest_framework.response import Response

from post.models import Post
from post.serializers import LikedUsersSerializer, PostSerializer


class PostServices:

    def list_services(self, user):
        # all posts
        queryset = Post.objects.all()
        if user.is_staff:
            # when user is admin all posts are shown without any sorting
            queryset = queryset
        else:
            # tag names that are liked but the user
            user_liked_tags = self.user_liked_tags(user=user)

            # ids of posts that are liked by user
            user_liked_post_ids = self.user_liked_post_ids(user=user)

            # extracting the most occurring tag from user liked tags
            most_liked_tag = self.most_frequent(user_liked_tags)

            # posts that are to be shown on the top based on the most liked tag by user
            priority_posts = Post.objects.filter(tags__slug__in=most_liked_tag).exclude(id__in=user_liked_post_ids)

            # least priority post based on user un-liked tags
            least_priority__posts = queryset.exclude(tags__slug__in=most_liked_tag)

            # posts that are already liked by the user
            liked_posts = queryset.filter(id__in=user_liked_post_ids)

            '''
            posts are now ordered in such as priority posts are on the top,
            then un-liked/least priority posts 
            and already liked post at the end
            '''
            queryset = chain(priority_posts, least_priority__posts, liked_posts)

        serializer = PostSerializer(queryset, context={'user': user}, many=True)

        return Response({
            'return': True,
            'message': 'Post list fetched successfully',
            'posts': serializer.data,
        },
            status=status.HTTP_200_OK
        )

    def user_liked_tags(self, user):
        # tag are extracted from the user liked posts
        posts = Post.votes.all(user.id).values_list('tags__slug')
        # tag name list
        return [i[0] for i in posts]

    def user_liked_post_ids(self, user):
        # extracting ids of user liked posts
        post_ids = Post.votes.all(user.id).values_list('id')
        # post id list
        return [i[0] for i in post_ids]

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
            # post object
            post = Post.objects.get(id=post_id)
            # users who liked the post
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
            },
                status=status.HTTP_204_NO_CONTENT
            )
        return Response({
            'return': False,
            'message': f'No posts with id: {post_id} found'
        },
            status=status.HTTP_404_NOT_FOUND
        )

    def most_frequent(self, list):
        '''
        :param list:
        :return: the most frequent value in a list
        '''
        if len(list) > 0:
            return [max(set(list), key=list.count)]
        return []
