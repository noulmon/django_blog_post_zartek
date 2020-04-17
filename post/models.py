from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from vote.models import VoteModel

from user.models import User


class Post(VoteModel, models.Model):
    title = models.CharField(max_length=25, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    tags = TaggableManager()
    created_by = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'POST'
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return "{}".format(self.title)


class PostImage(models.Model):
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False, upload_to='images/post_images/')

    class Meta:
        db_table = 'POST_IMAGE'
        verbose_name = _('post_image')
        verbose_name_plural = _('post_images')
