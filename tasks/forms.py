from django import forms

from . import models


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        exclude = ('slug', 'created', 'updated', 'employer')
