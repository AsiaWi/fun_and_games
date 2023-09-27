from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Activity, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ActivityForm, CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
# from django.contrib.auth.decorators import login_required, user_passes_test // like function
# from django.http import HttpResponseForbidden   / like function


# Create your views here.

class IndexView(TemplateView):
    template_name = 'playground/index.html'


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
        messages.add_message(self.request, messages.SUCCESS, 'Your post has been saved!')
        return super(AddActivity, self).form_valid(form)

class DeleteActivity(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    def test_func(self):
        return self.request.user == self.get_object().author
    
    model = Activity
    success_url = '/profile/'

    def get_object(self, queryset=None):
        activity_id = self.kwargs.get('activity_id')
        return Activity.objects.get(pk=activity_id)
        
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post deleted successfully!")
        return super().delete(request, *args, **kwargs)

class UpdateActivity(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Activity
    success_url = '/profile/'
    form_class = ActivityForm
    template_name = 'playground/edit_activity.html'

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_object(self, queryset=None):
        activity_id = self.kwargs.get('activity_id')
        return Activity.objects.get(pk=activity_id)

    def form_valid(self, form):
        # success message
        messages.success(self.request, 'Post updates saved!')
        return super().form_valid(form)


class DisplayActivityList(ListView):
    model = Activity
    template_name = 'playground/activities.html'
    paginate_by = 3
    context_object_name = 'activities'


class DisplayProfileWall(ListView):
    model = Activity
    template_name = 'playground/profile_wall.html'
    context_object_name = 'activities'
    paginate_by = 3


class DisplayActivityDetails(DetailView):
    model = Activity
    template_name = 'playground/view_activity_details.html'
    context_object_name = 'activity'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_comment_form'] = self.form_class()
        context['comments'] = Comment.objects.filter(activity=self.object)
        # likes
        check_likes = get_object_or_404(Activity, id=self.kwargs['pk'])
        liked = False
        if check_likes.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_num_of_likes'] = check_likes.total_num_of_likes()
        context['activity_liked'] = liked
        return context

    def post(self, request, *args, **kwargs):
        activity = self.get_object()
        form = self.form_class(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_author = self.request.user
            comment.activity = activity
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been posted!')
            return HttpResponseRedirect(reverse('view_activity_details', kwargs={'pk': activity.pk}))
        else:
            return self.render_to_response(self.get_context_data(form=form))

# @login_required // like function
# @user_passes_test(lambda user: user.is_authenticated, login_url=None)// like function
def ActivityLike(request, pk):
    activity = get_object_or_404(Activity, id=request.POST.get('activity_id'))
    if activity.likes.filter(id=request.user.id).exists():
        activity.likes.remove(request.user)
    else:
        activity.likes.add(request.user)

    return HttpResponseRedirect(reverse('view_activity_details', args=[str(pk)]))