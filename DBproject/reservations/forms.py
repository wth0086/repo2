from django import forms


class ReservationForm(forms.Form):
    Start_Date = forms.DateField(widget=forms.SelectDateWidget)
    End_Date = forms.DateField(widget=forms.SelectDateWidget)
