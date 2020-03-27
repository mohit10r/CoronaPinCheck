from django import forms

class PinForm(forms.Form):
    your_pin = forms.IntegerField(label='Enter your Pin')