from django import forms


class operat(forms.Form):
    STATUS_CHOICES = (
    ('+', ("+")),
    ('-', ("-")),
    ('*', ("*")),
    ('/', ("/")))
    num1 = forms.FloatField()
    operation = forms.ChoiceField(choices = STATUS_CHOICES, required=True)
    num2 = forms.FloatField()