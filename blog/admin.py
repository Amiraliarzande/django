from django.contrib import admin
from blog.models import post

# Register your models here.
class postAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title', 'counted_viwe', 'status', 'published_date', 'created_date', 'updated_date')
    list_filter = ('status',)
    search_fields = ['title', 'content']


admin.site.register(post, postAdmin)
