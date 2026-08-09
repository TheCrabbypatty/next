from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .api import get_next_task_from_ai
from .models import Task

# Create your views here.
@login_required
def main(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "interface/index.html", {"tasks": tasks})

@login_required
def add_task_view(request):
    if request.method == "POST":
        Task.objects.create(
            user=request.user,
            name=request.POST.get("task_name"),
            estimated_time=request.POST.get("task_time")
        )
    return redirect("main")

@login_required
def delete_task_view(request, task_id):
    Task.objects.filter(id=task_id, user=request.user).delete()
    return redirect("main")

@login_required
def next_task_view(request):
    tasks = Task.objects.filter(user=request.user)

    if not tasks.exists():
        return render(request, "interface/next_task.html", {
            "result": "You have no tasks yet."
        })

    result = get_next_task_from_ai(tasks)

    return render(request, "interface/next_task.html", {
        "result": result
    })


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect("/")  
    else:
        form = UserCreationForm()

    return render(request, "interface/register.html", {"form": form})

@login_required
def next_task_view(request):
    tasks = Task.objects.filter(user=request.user)

    if not tasks.exists():
        return render(request, "interface/next_task.html", {
            "result": "You have no tasks yet."
        })

    result = get_next_task_from_ai(tasks)

    return render(request, "interface/next_task.html", {
        "result": result
    })