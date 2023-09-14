from django.urls import path
from .views import post_views

app_name = 'bit_posts'

urlpatterns = [
    path('', post_views.PostListView.as_view(), name='post-list-create'),
    path('api/posts/', post_views.PostCreateAPIView.as_view(), name='api-post-create'),  # API endpoint for creating posts
    path('posts/<int:post_id>/upvote/', post_views.upvote_post, name='upvote_post'),  # Use post_views
    path('posts/<int:post_id>/remove_upvote/', post_views.remove_upvote_post, name='remove_upvote_post'),  # Use post_views
]
