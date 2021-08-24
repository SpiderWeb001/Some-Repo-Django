from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from loginpage.models import Post
from loginpage.forms import PostForm
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, "homepage.html", {'posts':posts} )

def login(request):
    return render(request,"login.html")

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # return HttpResponse(post)
    return render(request, "page.html", {'post': post})


def post_create(request):
    form = PostForm()
    return render(request, "post_create.html", {'form': form})

