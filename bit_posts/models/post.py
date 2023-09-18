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
            
#model for comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"