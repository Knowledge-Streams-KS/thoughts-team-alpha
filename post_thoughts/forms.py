from django import forms 
from post_thoughts.models import Thought

class Thought_ShareForm(forms.Form):
    username = forms.CharField(label="username", required=True)
    title = forms.CharField(label="title", required=True)
