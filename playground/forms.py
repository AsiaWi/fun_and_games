from .models import Activity
from django import forms
from djrichtextfield.widgets import RichTextWidget


class ActivityForm(forms.ModelForm):
    '''
    Create form to add Activity
    '''
    class Meta:
        model = Activity
        fields = ['title', 'excerpt', 'featured_image', 'image_alt', 'content', 'link', 'privacy']
        content = forms.CharField(widget=RichTextWidget())

        labels = {
            'title': 'Activity Title',
            'excerpt': 'Post Teaser',
            'featured_image': 'Add Image',
            'image_alt': 'Image Description',
            'content': 'Describe Activity',
            'link': 'Can you leave a website link?',
            'privacy': 'Publish post?'
        }
