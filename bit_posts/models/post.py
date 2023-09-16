from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=255,
    )

    content = models.TextField(
        _('Text')
    )

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    upvotes = models.ManyToManyField(
        get_user_model(),
        related_name='upvoted_posts',
        blank=True,
    )

    def upvote(self, user):
        """
        Upvote the post by a user.
        """
        if user not in self.upvotes.all():
            self.upvotes.add(user)
            self.save()

    def remove_upvote(self, user):
        """
        Remove upvote from the post by a user.
        """
        if user in self.upvotes.all():
            self.upvotes.remove(user)
            self.save()
            
    