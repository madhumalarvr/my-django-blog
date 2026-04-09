from django.shortcuts import render,redirect
from .models import Task

def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("/")

    tasks = Task.objects.all()
    return render(request, 'todo/home.html', {'tasks': tasks})


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("/")

# Create your views here.
