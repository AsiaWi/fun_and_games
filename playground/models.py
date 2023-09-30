from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django_quill.fields import QuillField
from django.utils import timezone


PRIVACY = (
    ('private', 'Keep it private'),
    ('public', 'Make it public')
)


class Activity(models.Model):
    '''
    PostActivity model to create and display entries added by users
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='post_author')
    title = models.CharField(max_length=100, null=False, blank=False)
    excerpt = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    featured_image = ResizedImageField(size=[400, None], quality=100,
                                       upload_to='activities/',
                                       force_format='WEBP',
                                       blank=False, null=False)
    image_alt = models.CharField(max_length=200, null=False, blank=False)
    content = QuillField(blank=False)
    link = models.CharField(max_length=200, default=None, blank=True)
    privacy = models.CharField(max_length=10, choices=PRIVACY,
                               default='private')
    likes = models.ManyToManyField(User, default=None, blank=True,
                                   related_name='like')

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def total_num_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE,
                                 related_name='comment')
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f'Comment by {self.comment_author.username}\
        under{self.activity.title}'
