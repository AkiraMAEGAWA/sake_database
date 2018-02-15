from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from sake_recommender.models import Sake
# Create your views here.

class SakeListView(TemplateView):
    template_name = "sake_list.html"

    def get(self, request, *args, **kwargs):
        context = super(SakeListView, self).get_context_data(**kwargs)

        sake = Sake.objects.all()
        context['sakes'] = sake
        return render(self.request, self.template_name, context)