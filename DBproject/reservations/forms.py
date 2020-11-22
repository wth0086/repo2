from django import forms
from django.utils import timezone
from . import models


class ReservationForm(forms.Form):
    Start_Date = forms.DateField(widget=forms.SelectDateWidget)
    End_Date = forms.DateField(widget=forms.SelectDateWidget)

    def clean(self):
        Start_Date = self.cleaned_data.get("Start_Date")
        End_Date = self.cleaned_data.get("End_Date")


class Reservate(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = (  # 기존의 위젯을 살릴 방법이 없을까?
            "user",
            "checkin",
            "checkout",
            "roomtype",
            "bedtype",
            "card",
            "cardNum",
            "cardExpYear",
            "cardExpMonth",
            "additionalService",
        )

    def save(self, *args, **kwargs):
        reservation = super().save(commit=False)
        reservation.created = timezone.now()
        reservation.updated = timezone.now()
        reservation.user = self.cleaned_data.get("user")
        reservation.checkin = self.cleaned_data.get("checkin")
        reservation.checkout = self.cleaned_data.get("checkout")
        reservation.roomtype = self.cleaned_data.get("roomtype")
        reservation.bedtype = self.cleaned_data.get("bedtype")
        reservation.card = self.cleaned_data.get("card")
        reservation.cardExpYear = self.cleaned_data.get("cardExpYear")
        reservation.cardExpMonth = self.cleaned_data.get("cardExpMonth")
        reservation.additionalService = self.cleaned_data.get(
            "additionalService"
        )  # 값이 여러개 들어가는게 어떻게 해야는거지
        reservation.save()
