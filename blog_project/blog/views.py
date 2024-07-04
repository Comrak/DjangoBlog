# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth import logout
from django.urls import reverse    
from django.http import HttpResponseRedirect






def mostrar_ultimos_posts(request):
   
    ultimos_posts = Post.objects.order_by('-created_at')[:10]  
    for post in ultimos_posts:
        post.total_likes = post.total_likes()
        post.liked = post.likes.filter(id=request.user.id).exists()
    return render(request, 'mostrar_posts.html', {'ultimos_posts': ultimos_posts})



def index(request):
   
 ultimos_posts = Post.objects.order_by('-created_at')[:10] 
 for post in ultimos_posts:
        post.total_likes = post.total_likes()
        post.liked = post.likes.filter(id=request.user.id).exists()
 return render(request, 'blog/index.html', {'ultimos_posts': ultimos_posts})


def post_list(request):
    posts = Post.objects.all()
    latest_post = Post.objects.filter(author=request.user).order_by('-created_at').first()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    total_likes = post.total_likes()
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
  
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            total_likes = post.total_likes()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
        return render(request, 'blog/post_detail.html', {'post': post, 'comment_form': comment_form, 'total_likes': total_likes,'liked': liked })

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def latest_post(request):
    latest_post = Post.objects.filter(author=request.user).order_by('-created_at').first()
    return render(request, 'blog/latest_post.html', {'latest_post': latest_post})





@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('post_list')

def profile(request):
    return render(request, 'profile.html')



def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
