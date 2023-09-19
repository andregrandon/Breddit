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
from bit_posts.models.post import Comment, Post, SubComment
from django.contrib import messages
from bit_posts.forms.forms import CommentForm, ReplyToCommentForm  
from bit_posts.serializers import post_serializers
from django.contrib import messages
from django.urls import reverse_lazy, reverse 
from django.db.models import Count

#  #  # POSTS #  #  #

# Posts API
class PostListView(generics.ListCreateAPIView):
    serializer_class = post_serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all().order_by('-created_at')

    def list(self, request, *args, **kwargs):
        filter_type = request.GET.get('filter', 'recent')  

        if filter_type == 'likes':
            queryset = self.get_queryset().annotate(upvotes_count=Count('upvotes')).order_by('-upvotes_count', '-created_at')
        elif filter_type == 'comments':
            queryset = self.get_queryset().annotate(comments_count=Count('comments')).order_by('-comments_count', '-created_at')
        else:
            queryset = self.get_queryset().order_by('-created_at')

        return render(request, 'bit_posts/posts.html', {'object_list': queryset})


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = post_serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
# Edit Posts
class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'bit_posts/edit_post.html'  # Create an edit_post.html template
    fields = [ 'title','content']  
    
    def get_success_url(self):
        return reverse('bit_posts:post-list-create')
    

# Delete Posts
class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'bit_posts/delete_post.html'  
    success_url = reverse_lazy('bit_posts:post-list-create')  
    
    

# API Finds Post By ID
@api_view(['POST'])
def get_post_by_id(request):
    try:
        post_id = request.data.get('post_id')
        post = Post.objects.get(id=post_id)
        serializer = post_serializers.PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
def retrieve_view(request):
    return render(request, 'bit_posts/find_by_id.html')
    




#  #  # COMMENTS #  #  #

# Create Comment
def create_comment(request, post_id, comment_id=None):
    post = get_object_or_404(Post, pk=post_id)

    if not request.user.is_authenticated:
        # If the user is not logged in, add an error message and redirect them
        messages.error(request, 'You must be logged in to comment.')
        return redirect('bit_users:login')  

    parent_comment = None

    if comment_id:
        parent_comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.parent_comment = parent_comment  
            comment.save()
            return redirect('create-comment', post_id=post_id)  
        else:
          
            messages.error(request, 'There was an error with your comment. Please correct it.')

    else:
        form = CommentForm()

    comments = Comment.objects.filter(post=post, parent_comment=None).order_by('-created_at')
    # Filter only top-level comments for the post 
    
    context = {
        'form': form,
        'post': post,
        'post_id': post_id,
        'comments': comments,
    }

    return render(request, 'bit_posts/create_comment.html', context)



# Delete Comment
def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
        
        # Check if the user is authorized to delete the comment

        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
    except Comment.DoesNotExist:
        messages.success(request, 'Comment deleted.')
    except Exception as e:
        messages.error(request, f'Error deleting comment: {str(e)}')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Edit Comments 
class UpdateComment(UpdateView):
    model = Comment
    template_name = 'bit_posts/edit_comment.html'  
    fields = ['text']  
    
    def get_success_url(self):
       
        return reverse('bit_posts:create-comment', kwargs={'post_id': self.object.post.pk})



#  #  # Upvote API #  #  #

# Upvote Api
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if post.upvotes.filter(id=user.id).exists():
      
        post.upvotes.remove(user)
        message = 'Upvote removed successfully.'
        liked = False  
    else:
       
        post.upvotes.add(user)
        message = 'Upvoted successfully.'
        liked = True  

    post.save()

    new_like_count = post.upvotes.count

    referring_page = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(referring_page)





#  #  # REPLIES/SUBCOMMENTS FOR COMMENTS #  #  #


# Create Replies
def create_subcomment(request, parent_comment_id):
    parent_comment = get_object_or_404(Comment, id=parent_comment_id)

    if request.method == 'POST':
        form = ReplyToCommentForm(request.POST)
        if form.is_valid():
            subcomment = form.save(commit=False)
            subcomment.user = request.user
            subcomment.parent_comment = parent_comment
            subcomment.post = parent_comment.post 
            subcomment.is_reply = True  
            subcomment.save()
            
            return redirect('bit_posts:create-comment', post_id=parent_comment.post.id)

    subcomments = SubComment.objects.filter(parent_comment=parent_comment).order_by('-created_at')  

    form = ReplyToCommentForm()
    
    return render(request, 'bit_posts/reply_comment.html', {'form': form, 'parent_comment': parent_comment, 'subcomments': subcomments})
    

# Delete Replies 
def delete_subcomment(request, subcomment_id):
    try:
        subcomment = SubComment.objects.get(pk=subcomment_id)
        
        subcomment.delete()
        messages.success(request, 'Subcomment deleted successfully.')
    except SubComment.DoesNotExist:
        messages.success(request, 'Subcomment deleted.')
    except Exception as e:
        messages.error(request, f'Error deleting subcomment: {str(e)}')

  
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Update Replies
class UpdateSubcomment(UpdateView):
    model = SubComment  
    template_name = 'bit_posts/edit_subcomment.html'  
    fields = ['text']  

    def get_success_url(self):
        return reverse('bit_posts:create-comment', kwargs={'post_id': self.object.parent_comment.post.pk})
    




