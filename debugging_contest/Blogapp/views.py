from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from .form import PostForm


def index(request):
    post = Post.objects
    return render(request, 'index.html', {'post':post})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post})

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('index')

def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/post/'+ str(post.id))
    else:
        form = PostForm()
        return render(request, 'new.html', {'forms':form})

def edit(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/post/'+str(post.id))
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})
