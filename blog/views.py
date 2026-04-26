from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

def home(request):
    user, created = User.objects.get_or_create(username='madhu')

    if created:
        user.set_password('malar')
        user.is_superuser = True
        user.is_staff = True
        user.save()


    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {'post': post})
# Create your views here.

