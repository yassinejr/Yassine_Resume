from django.contrib import admin
from .models import ContactForm


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'


admin.site.register(ContactForm, ContactAdmin)
# Register your models here.
