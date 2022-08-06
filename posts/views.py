from django.shortcuts import render

# Create your views here.
from .models import Post

def allPosts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {"posts": posts}) 

def singlePost(request, id):
    post = Post.objects.get(id=id)
    return render(request, "post.html", {"post": post})