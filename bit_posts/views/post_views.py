from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from bit_posts.models import Post
from bit_posts.serializers import post_serializers


class PostListView(generics.ListCreateAPIView):
    serializer_class = post_serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all().order_by('-created_at')

    def list(self, request, *args, **kwargs):
        # Get the queryset data
        queryset = self.filter_queryset(self.get_queryset())

        # Render the HTML template and pass the data to it
        return render(request, 'bit_posts/posts.html', {'object_list': queryset})

class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = post_serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if post.upvotes.filter(id=user.id).exists():
        # User has already upvoted, remove their upvote
        post.upvotes.remove(user)
        post.save()
        print(f'User {user.username} removed their upvote for post {post.id}')
        return Response({'message': 'Upvote removed successfully.'}, status=status.HTTP_200_OK)
    else:
        # User hasn't upvoted, add their upvote
        post.upvotes.add(user)
        post.save()
        print(f'User {user.username} upvoted post {post.id}')
        return Response({'message': 'Upvoted successfully.'}, status=status.HTTP_201_CREATED)
@permission_classes([permissions.IsAuthenticated])
def remove_upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if post.upvotes.filter(id=user.id).exists():
        # User has upvoted, remove their upvote
        post.upvotes.remove(user)
        post.save()
        return Response({'message': 'Upvote removed successfully.'}, status=status.HTTP_200_OK)
    else:
        # User hasn't upvoted, return a message indicating they haven't upvoted
        return Response({'message': 'You have not upvoted this post.'}, status=status.HTTP_400_BAD_REQUEST)
    

def find_by_id_view(request):
    return render(request, 'bit_posts/find_by_id.html')

#*** function to retrieve post ID ****  





def render_posts(request):
    error_message = None
    post = None

    if 'post_id' in request.GET:
        post_id = request.GET['post_id']
        try:
            # Attempt to retrieve the post by ID
            post_id = int(post_id)  # Convert to integer
            post = Post.objects.get(id=post_id)
        except (Post.DoesNotExist, ValueError):
            error_message = "No post found with the provided ID."

    # If post is found, render the post template, otherwise render a template with the error message
    if post:
        return render(request, 'bit_posts/find_by_id.html', {'post': post})
    else:
        return render(request, 'bit_posts/find_by_id.html', {'error_message': error_message})









def find_post_by_id_view(request):
    # Handle the form submission here and return the appropriate response
    # You can access the submitted data using request.POST.get('post_id')
    # Perform the necessary logic to find the post by ID

    # For example, you can render a template with the results or perform a redirect
    return render(request, 'bit_posts/find_post_result.html', {'post': find_by_id_view})

