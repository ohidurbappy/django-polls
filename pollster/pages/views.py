from django.shortcuts import render
from django.views import generic

from .models import Page

class IndexView(generic.ListView):
    template_name="pages/index.html"
    context_object_name="list_of_pages"

    def get_queryset(self):
        return Page.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model=Page
    template_name="pages/detail.html"
