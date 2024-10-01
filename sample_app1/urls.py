from django.urls import path

from .views import SubmitFormView

urlpatterns = [
    path("api/submit-form/", SubmitFormView.as_view(), name="submit-form"),
]
