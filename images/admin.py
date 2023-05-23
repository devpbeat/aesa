from django.contrib import admin
from .models import Images

# Register your models here.
admin.site.site_header = "Images Administration"
admin.site.site_title = "Images Administration"
admin.site.index_title = "Images Administration"
admin.site.register(Images)