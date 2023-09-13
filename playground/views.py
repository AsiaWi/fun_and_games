from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Activity
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(TemplateView):
    template_name = 'playground/index.html'

class AddActivity(LoginRequiredMixin, CreateView):
    '''
    class based view to add post by user
    '''
    template_name = 'playground/add_activity.html'
    model = Activity
    success_url = '/playground/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddActivity, self).form_valid(form)