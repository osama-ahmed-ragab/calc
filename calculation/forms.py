from django import forms


class operat(forms.Form):
    num1 = forms.FloatField()
    operation = forms.CharField()
    num2 = forms.FloatField()