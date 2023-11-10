from django.shortcuts import render
from django.views import generic
from .models import Nike , Review




# Create your views here.

class NikeList(generic.ListView):
    model = Nike
    paginate_by = 8



class NikeDetail(generic.DetailView):
    model = Nike    