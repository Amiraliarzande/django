from django.contrib import admin
from website.models import Contact,Newsletter
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date','message','updated_date')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_date',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)