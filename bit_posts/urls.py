from django.urls import path
from .views import post_views 


app_name = 'bit_posts'

urlpatterns = [
    path('', post_views.PostListView.as_view(), name='post-list-create'),
    path('api/posts/', post_views.PostCreateAPIView.as_view(), name='api-post-create'),  
    path('post/<int:post_id>/create-comment/', post_views.create_comment, name='create-comment'),
    path('delete-comment/<int:comment_id>/', post_views.delete_comment, name='delete-comment'),
    path('edit-comment/<int:pk>/edit/', post_views.UpdateComment.as_view(), name='edit-comment'),  
    path('api/post/<int:post_id>/upvote/', post_views.upvote_post, name='upvote-post'),
    path('post-update/<int:pk>/', post_views.UpdatePost.as_view(), name='update-post'),
    path('post-delete/<int:pk>/', post_views.DeletePost.as_view(), name='delete-post'),
    path('post/<int:parent_comment_id>/reply/', post_views.create_subcomment, name='reply-comment'),
    path('subcomment/<int:subcomment_id>/delete/', post_views.delete_subcomment, name='delete-subcomment'),
    path('subcomment/<int:pk>/update/', post_views.UpdateSubcomment.as_view(), name='update-subcomment'),
    path('api/get-post-by-id/', post_views.get_post_by_id, name='get-post-by-id'),
    path('retrieve/', post_views.retrieve_view, name='find-by-id'), 
]



