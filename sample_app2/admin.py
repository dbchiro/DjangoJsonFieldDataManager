from django.contrib import admin

from .models import SampleApp2A, SampleApp2B

# Register your models here.
admin.site.register(SampleApp2A, admin.ModelAdmin)
admin.site.register(SampleApp2B, admin.ModelAdmin)
