from rest_framework import serializers

from .models import AllowedKey


class AllowedKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = AllowedKey
        fields = "__all__"
