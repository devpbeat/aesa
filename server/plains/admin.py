from django.contrib import admin
from .models import Plain

# Register your models here.
admin.site.site_header = "Plain Administration"
admin.site.site_title = "Plain Administration"
admin.site.index_title = "Plain Administration"
admin.site.register(Plain)