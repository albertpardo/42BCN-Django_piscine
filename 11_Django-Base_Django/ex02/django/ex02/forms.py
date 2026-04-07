from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(label='Escribe algo', max_length=100)
