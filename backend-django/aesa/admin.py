from django.contrib import admin

from .models import Plain, Project

admin.site.register(Project)
admin.site.register(Plain)
