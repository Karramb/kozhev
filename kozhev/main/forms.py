from django import forms


class ApplicationForm(forms.Form):
    name = forms.CharField(label='Ваше имя:', max_length=100)
    email = forms.EmailField(label='Электронная почта:')
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label='Сообщение:')