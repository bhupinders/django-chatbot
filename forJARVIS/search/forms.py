from django import forms

class MyForm(forms.Form):
    answer_this = forms.CharField(max_length=100)
