from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path("reservation", views.ReservationView.as_view(), name="reservation"),
    path("reservate", views.Reservate.as_view(), name="reservate"),
]
