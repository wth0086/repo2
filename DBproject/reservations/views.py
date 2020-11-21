from django.views.generic import FormView
from django.urls import reverse_lazy
from . import forms
from .models import BookedDay


class ReservationView(FormView):
    template_name = "reservations/reservation.html"
    form_class = forms.ReservationForm


class Reservate(FormView):
    template_name = "reservations/reservate.html"
    form_class = forms.Reservate
    success_url = reverse_lazy("reservations:reservate")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)