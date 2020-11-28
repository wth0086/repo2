from django.shortcuts import render


def coreView(request):
    return render(request, "cores/home.html", {})
