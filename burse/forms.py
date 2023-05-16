from django import forms


class ReplayFrom(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Комментарий...'}))


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())