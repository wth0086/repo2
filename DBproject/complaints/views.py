from django.shortcuts import render
from .models import Complain


def complaints(request):
    complains = Complain.object.all()
    return render(request, "complaints/complaint.html", {"complain_list": complains})


def complain_text(request):
    return render(request, "complaints/complain_text.html")
