from django.contrib import admin

from .forms import AllowedKeyForm
from .models import AllowedKey


@admin.register(AllowedKey)
class AllowedKeyAdmin(admin.ModelAdmin):
    form = AllowedKeyForm
    list_display = ("model_name", "key", "value_type", "hidden")
    search_fields = ("model_name", "key")
