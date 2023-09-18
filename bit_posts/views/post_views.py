from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework import permissions
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from bit_posts.models.post import Comment 
from bit_posts.models.post import Post
from django.contrib import messages
from bit_posts.forms.forms import CommentForm  
from bit_posts.serializers import post_serializers
from django.contrib import messages
from django.urls import reverse_lazy, reverse 
from django.db.models import Count

class PostListView(generics.ListCreateAPIView):
    serializer_class = post_serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all().order_by('-created_at')

    def list(self, request, *args, **kwargs):
        filter_type = request.GET.get('filter', 'recent')  # Get the filter type from query parameters

        if filter_type == 'likes':
            queryset = self.get_queryset().annotate(upvotes_count=Count('upvotes')).order_by('-upvotes_count', '-created_at')
        elif filter_type == 'comments':
            queryset = self.get_queryset().annotate(comments_count=Count('comments')).order_by('-comments_count', '-created_at')
        else:
            queryset = self.get_queryset().order_by('-created_at')

        # Render the HTML template and pass the data to it
        return render(request, 'bit_posts/posts.html', {'object_list': queryset})

class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = post_serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

def find_by_id_view(request):
    return render(request, 'bit_posts/find_by_id.html')

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
    return render(request, 'bit_posts/find_post_result.html', {'post': find_by_id_view})



def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if not request.user.is_authenticated:
        # If the user is not logged in, add an error message and redirect them
        messages.error(request, 'You must be logged in to comment.')
        return redirect('bit_users:login')  # Replace 'login' with the actual URL name for your login view

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Assign the logged-in user
            comment.post = post
            comment.save()
            # Redirect to the post detail page after saving the comment
            return redirect('create-comment', post_id=post_id)  # Replace 'post-detail' with your actual URL name
        else:
            # If the form is not valid, add an error message
            messages.error(request, 'There was an error with your comment. Please correct it.')

    else:
        form = CommentForm()

    comments = Comment.objects.filter(post=post, parent_comment__isnull=True)  # Get comments for the post

    context = {
        'form': form,
        'post': post,
        'post_id': post_id,
        'comments': comments,
    }

    return render(request, 'bit_posts/create_comment.html', context)


def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
        
        # Check if the user is authorized to delete the comment, and perform the deletion.
        # ...

        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
    except Comment.DoesNotExist:
        messages.success(request, 'Comment deleted.')
    except Exception as e:
        messages.error(request, f'Error deleting comment: {str(e)}')

    # Redirect back to the current page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if post.upvotes.filter(id=user.id).exists():
        # User has already upvoted, remove their upvote (unlike)
        post.upvotes.remove(user)
        message = 'Upvote removed successfully.'
        liked = False  # User unliked the post
    else:
        # User hasn't upvoted, add their upvote (like)
        post.upvotes.add(user)
        message = 'Upvoted successfully.'
        liked = True  # User liked the post

    post.save()

    # Get the updated like count
    new_like_count = post.upvotes.count

    referring_page = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(referring_page)


# Edit Main Posts
class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'bit_posts/edit_post.html'  # Create an edit_post.html template
    fields = [ 'title','content']  # Add fields you want to edit
    
    def get_success_url(self):
        # Redirect to the create-comment page for the edited comment's post
        return reverse('bit_posts:post-list-create')
    

# Delete Main Posts
class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'bit_posts/delete_post.html'  # Create a delete_post.html template
    success_url = reverse_lazy('bit_posts:post-list-create')  # Redirect after deleting


class UpdateComment(UpdateView):
    model = Comment
    template_name = 'bit_posts/edit_comment.html'  # Replace with your actual template name
    fields = ['text']  # Update with the fields you want to edit

    def get_success_url(self):
        # Redirect to the create-comment page for the edited comment's post
        return reverse('bit_posts:create-comment', kwargs={'post_id': self.object.post.pk})
    