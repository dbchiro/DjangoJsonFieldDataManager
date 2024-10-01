from django.contrib import admin

from .models import SampleApp1

# Register your models here.
admin.site.register(SampleApp1, admin.ModelAdmin)
