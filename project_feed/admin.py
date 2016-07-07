from django.contrib import admin

from .models import Organization, Project, ProjectUpdate, Tag

admin.site.register(Organization)
admin.site.register(Project)
admin.site.register(ProjectUpdate)
admin.site.register(Tag)

# Register your models here.
