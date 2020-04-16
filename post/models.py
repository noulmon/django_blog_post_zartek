from django.db import models
from django.utils.translation import ugettext_lazy as _
from vote.models import VoteModel

from user.models import User


class Post(VoteModel, models.Model):
    title = models.CharField(max_length=15, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_by = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=False, blank=False)

    class Meta:
        db_table = 'POST'
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return "{}".format(self.title)
