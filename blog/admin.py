from django.contrib import admin
from blog.models import post , Category, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class postAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title','author','counted_viwe', 'status', 'published_date', 'created_date', 'updated_date')
    list_filter = ('status','author')
    search_fields = ['title', 'content','author']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'subject', 'created_date', 'updated_date', 'approved')
    search_fields = ['post__title', 'name', 'email', 'subject']
    list_filter = ('created_date', 'approved')


admin.site.register(Category)
admin.site.register(post, postAdmin)
admin.site.register(Comment, CommentAdmin)

