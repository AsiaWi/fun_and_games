from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from PIL import Image, ImageFile, ImageOps, ExifTags
from django_quill.fields import QuillField

# Create your models here.

PRIVACY = (
    ('private', 'Private'),
    ('public', 'Public')
)
class Activity(models.Model):
    '''
    PostActivity model to create and display entries added by users
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=100, null=False, blank=False)
    excerpt = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    featured_image = ResizedImageField(size=[400, None], quality=100, upload_to='activities/', force_format='WEBP', blank=False, null=False)
    image_alt = models.CharField(max_length=200, null=False, blank=False)
    content = QuillField()
    link = models.CharField(max_length=200, null=True)
    privacy = models.CharField(max_length=10, choices=PRIVACY, default='private')
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


