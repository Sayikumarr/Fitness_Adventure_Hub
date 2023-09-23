from django.contrib import admin
from .models import Configuration
from .models import BlogPost, Activity, ContactFormSubmission

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Activity)
admin.site.register(ContactFormSubmission)

@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')


from django.contrib import admin

admin.site.site_title = "SHAREEF'S FITNESS & ADVENTURE HUB"  # Set the title for the admin site
admin.site.site_header = "SHAREEF'S FITNESS & ADVENTURE HUB"  # Set the header for the admin site