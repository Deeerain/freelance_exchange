from django import forms


class ReplayForm(forms.Form):
    comment = forms.CharField(max_length=1000, widget=forms.Textarea)