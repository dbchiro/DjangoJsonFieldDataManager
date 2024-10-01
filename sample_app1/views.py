from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView


class SubmitFormView(APIView):
    def post(self, request):
        # Process the submitted form data
        form_data = request.data
        # Here you can add your logic to handle the form data
        print(form_data)  # For demonstration purposes
        return Response(
            {"message": "Form submitted successfully!"},
            status=status.HTTP_200_OK,
        )
