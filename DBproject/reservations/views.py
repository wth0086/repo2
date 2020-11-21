from django.views.generic import FormView
from django.db.models import Q
from .forms import ReservationForm
from . import forms


class ReservationView(FormView):
    template_name = "reservations/reservation.html"
    form_class = forms.ReservationForm
