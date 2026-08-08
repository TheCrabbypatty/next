from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def main(request):
    return render(request, "interface/index.html")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect("/")  # send them to your main page
    else:
        form = UserCreationForm()

    return render(request, "interface/register.html", {"form": form})