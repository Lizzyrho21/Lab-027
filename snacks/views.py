from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from snacks import models as snack_models

# Create your views here.

# create SnackListView
class SnackListView(ListView):
    def get(self, request):
        return render(request, 'snack_list.html')

# extend ListView
# give a template of snack_list.html
# associate Snack model

