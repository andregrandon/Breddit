from django.urls import path

from .views import post_views

urlpatterns = [
    path('', post_views.PostListView.as_view(), name='post-list-create'),
]
