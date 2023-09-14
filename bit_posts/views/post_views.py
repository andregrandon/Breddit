from rest_framework import generics
from rest_framework import permissions

from bit_posts.models import Post
from bit_posts.serializers import post_serializers


class PostListView(generics.ListCreateAPIView):

    serializer_class = post_serializers.PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    queryset = Post.objects.all()
