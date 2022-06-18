from django import forms


time_choices = [
    ("01:00", "01:00"),
    ("02:00", "02:00"),
    ("03:00", "03:00"),
    ("04:00", "04:00"),
    ("05:00", "05:00"),
    ("06:00", "06:00"),
    ("07:00", "07:00"),
    ("08:00", "08:00"),
    ("09:00", "09:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
]

noon_choices = [("AM", "AM"), ("PM", "PM")]


class FareCalculatorForm(forms.Form):
    time = forms.TypedChoiceField(choices=time_choices)
    noon = forms.TypedChoiceField(choices=noon_choices)
    distance = forms.FloatField(min_value=0)
