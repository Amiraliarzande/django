from django.contrib import admin
from blog.models import post , Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class postAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title','author','counted_viwe', 'status', 'published_date', 'created_date', 'updated_date')
    list_filter = ('status','author')
    search_fields = ['title', 'content','author']
    summernote_fields = ('content',)

admin.site.register(Category)
admin.site.register(post, postAdmin)
