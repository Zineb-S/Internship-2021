from django import forms
from .models import PathFolder


class PathForm(forms.ModelForm):
    class Meta:
        model = PathFolder
        fields = ["path_to_folder", ]
