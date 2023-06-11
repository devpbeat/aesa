from django.contrib import admin
from .models import Project

# Register your models here.
admin.site.site_header = "Project Administration"
admin.site.site_title = "Project Administration"
admin.site.index_title = "Project Administration"
admin.site.register(Project)