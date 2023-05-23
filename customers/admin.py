from django.contrib import admin
from .models import Customer

# Register your models here.
admin.site.site_header = "Customer Administration"
admin.site.site_title = "Customer Administration"
admin.site.index_title = "Customer Administration"
admin.site.register(Customer)