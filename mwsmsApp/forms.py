from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["fullname", "mobile_number", "eaten", "slept", "content", ]
    labels = {'fullname': "Name", "mobile_number": "Mobile Number","eaten":"eaten", "slept":"slept", "content":"content"}