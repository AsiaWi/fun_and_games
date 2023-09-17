from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import Activity
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ActivityForm

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
    form_class = ActivityForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddActivity, self).form_valid(form)

class DisplayActivityList(ListView):
    model = Activity
    template_name = 'playground/index.html'
    paginate_by = 3
    context_object_name = 'activities'

class DisplayProfileWall(ListView):
    model = Activity
    template_name = 'playground/profile_wall.html'
    context_object_name = 'activities'

class DisplayActivityDetails(DetailView):
    model = Activity
    template_name = 'playground/view_activity_details.html'
    context_object_name = 'activity'
