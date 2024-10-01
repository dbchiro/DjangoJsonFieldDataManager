from django import forms
from django.apps import apps

from .models import AllowedKey, ExtraDataMixin


class AllowedKeyForm(forms.ModelForm):
    class Meta:
        model = AllowedKey
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate the model_name field with choices from models that inherit from ExtraDataMixin
        self.fields["model_name"] = forms.ChoiceField(
            choices=self.get_model_choices()
        )

    def get_model_choices(self):
        # Get all models in the current app
        app_label = "your_app_name"  # Replace with your app name
        models = apps.get_models()
        choices = [
            (model.__name__, model.__name__)
            for model in models
            if issubclass(model, ExtraDataMixin)
        ]
        return choices
