from django import forms
from replays.models import Replay


class ReplayForm(forms.ModelForm):
    comment = forms.CharField(max_length=1000, widget=forms.Textarea)

    class Meta:
        model = Replay
        fields = ('comment',)
