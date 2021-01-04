from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, Comment
# from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
# admin.site.register(BlogPost,MarkdownxModelAdmin)

class PostAdmin(SummernoteModelAdmin):
    # summernote_fields = '__all__'
    summernote_fields = ('body',)
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'created_at', 'body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(BlogPost,PostAdmin)
