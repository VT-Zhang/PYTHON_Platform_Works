from django.shortcuts import render, redirect

def index(request):
    return render(request, "nin/index.html")

def all(request):
    return render(request, "nin/all.html")

def color(request, color):
    context = {
        "color": color,
    }
    return render(request, "nin/color.html", context)
