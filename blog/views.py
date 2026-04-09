from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

def home(request):
    def home(request):
        if not User.objects.filter(username='madhu').exists():
            User.objects.create_superuser('madhu', 'madhu@email.com', '1234abcd')

        posts = Post.objects.all().order_by('-created_at')


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {'post': post})
# Create your views here.

