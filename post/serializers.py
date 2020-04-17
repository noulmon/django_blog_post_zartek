from rest_framework import serializers

from django_blog_post_zartek.settings import MEDIA_ROOT, MEDIA_URL
from post.models import Post, PostImage
from user.models import User
from user.serializers import UserSerializer
from datetime import datetime


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    created_by = serializers.CharField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    # images in the post
    images = serializers.SerializerMethodField()
    # number of likes the post have
    likes_no = serializers.SerializerMethodField()
    # usernames who had liked the post
    liked_users = serializers.SerializerMethodField()
    # checks whether the post is liked by a user or not
    is_liked = serializers.SerializerMethodField()

    def get_images(self, post):
        '''
        :param post: The post object.
        :return: The Images attached to the post.
        '''
        if PostImage.objects.filter(post=post).exists():
            post_images = PostImage.objects.filter(post=post).values_list('image')
            return [MEDIA_URL+image[0] for image in post_images]
        return None

    def get_likes_no(self, post):
        '''
        :param post: The post object.
        :return: The number of likes the post have(shown iff the user is admin).
        '''
        user = self.context.get('user')
        # checking if the user is admin
        if user.is_staff:
            return post.votes.count()
        return ''

    def get_liked_users(self, post):
        '''
        :param post: The post object.
        :return: The list of username who had liked the post(shown iff the user is admin).
        '''
        user = self.context.get('user')
        # checking if the user is admin
        if user.is_staff:
            users = post.votes.user_ids()
            if len(users) > 0:
                user_ids = [i[0] for i in users]
                return User.objects.filter(id__in=user_ids).values_list('username')
        return ''

    def get_is_liked(self, post):
        '''
        :param post: The post object.
        :return: Returns whether the post is liked by the user or not.
        '''
        user = self.context.get('user')
        return post.votes.exists(user.id)


class PostImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField()


class LikedUsersSerializer(serializers.Serializer):
    user = serializers.SerializerMethodField()
    liked_at = serializers.SerializerMethodField()

    def get_user(self, obj):
        user_id = obj[0]
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return serializer.data

    def get_liked_at(self, obj):
        date = obj[1]
        return date.strftime("%Y-%m-%d %H:%M:%S")
