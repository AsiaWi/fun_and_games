from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Activity, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ActivityForm, CommentForm
from django.urls import reverse_lazy

# Create your views here.


class AddActivity(LoginRequiredMixin, CreateView):
    '''
    class based view to add post by user
    '''
    template_name = 'playground/add_activity.html'
    model = Activity
    success_url = '/profile/'
    form_class = ActivityForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_activity_form'] = self.form_class()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddActivity, self).form_valid(form)


class DeleteActivity(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    def test_func(self):
        return self.request.user == self.get_object().author
    
    model = Activity
    success_url = '/profile/'

    def get_object(self, queryset=None):
        activity_id = self.kwargs.get('activity_id')
        return Activity.objects.get(pk=activity_id)


class UpdateActivity(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Activity
    success_url = '/profile/'
    form_class = ActivityForm
    template_name = 'playground/edit_activity.html'

    def get_object(self, queryset=None):
        activity_id = self.kwargs.get('activity_id')
        return Activity.objects.get(pk=activity_id)

    def test_func(self):
        return self.request.user == self.get_object().author


class DisplayActivityList(ListView):
    model = Activity
    template_name = 'playground/index.html'
    #paginate_by = 3
    context_object_name = 'activities'


class DisplayProfileWall(ListView):
    model = Activity
    template_name = 'playground/profile_wall.html'
    context_object_name = 'activities'


class DisplayActivityDetails(DetailView):
    model = Activity
    template_name = 'playground/view_activity_details.html'
    context_object_name = 'activity'
    form_class = CommentForm
    success_url = '/profile/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_comment_form'] = self.form_class()
        return context
    
    