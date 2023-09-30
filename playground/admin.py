from django.contrib import admin
from .models import Activity, Comment


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'featured_image',
        'image_alt',
        'content',
        'link',
        'privacy'

    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'activity',
        'comment_author',
        'comment_content',
        'created_date'
    )
