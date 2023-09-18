from django.urls import path
from .views import post_views 


app_name = 'bit_posts'

urlpatterns = [
    path('', post_views.PostListView.as_view(), name='post-list-create'),
    path('api/posts/', post_views.PostCreateAPIView.as_view(), name='api-post-create'),  # API endpoint for creating posts
    path('render-posts/', post_views.render_posts, name='render-posts'),    
    path('find-by-id/', post_views.find_by_id_view, name='find-by-id'),
    path('find-post-by-id/', post_views.find_post_by_id_view, name='find-post-by-id'),
    path('post/<int:post_id>/create-comment/', post_views.create_comment, name='create-comment'),
    path('delete-comment/<int:comment_id>/', post_views.delete_comment, name='delete-comment'),
    path('edit-comment/<int:pk>/edit/', post_views.UpdateComment.as_view(), name='edit-comment'),  # Edit a comment
    path('api/post/<int:post_id>/upvote/', post_views.upvote_post, name='upvote-post'),
    path('post-update/<int:pk>/', post_views.UpdatePost.as_view(), name='update-post'),
    path('post-delete/<int:pk>/', post_views.DeletePost.as_view(), name='delete-post'),
]



