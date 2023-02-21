
from django.shortcuts import render
from .models import MyModel
from .forms import MyForm

def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'mwsmsApp/index.html', {'form': form})