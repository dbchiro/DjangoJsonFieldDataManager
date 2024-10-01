from django.db import models

# from django.db.models import JSONField  # For Django 3.1+ users


class AllowedKey(models.Model):
    STRING = "string"
    NUMBER = "number"
    LIST = "list"
    DICT = "dict"

    VALUE_TYPE_CHOICES = [
        (STRING, "String"),
        (NUMBER, "Number"),
        (LIST, "List"),
        (DICT, "Dict"),
    ]
    INPUT_TYPE_CHOICES = [
        ("text", "Text"),
        ("number", "Number"),
        ("select", "Select"),
        ("select_multiple", "Select Multiple"),
        ("textarea", "Textarea"),
    ]
    model_name = models.CharField(max_length=100)
    key = models.CharField(max_length=100, unique=True)
    value_type = models.CharField(max_length=10, choices=VALUE_TYPE_CHOICES)
    expected_values = models.JSONField(default=list, blank=True, null=True)
    input_type = models.CharField(
        max_length=20, choices=INPUT_TYPE_CHOICES, default="text"
    )
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.model_name} - {self.key} ({self.value_type} - {self.input_type})"


class ExtraDataMixin(models.Model):
    extra_data = models.JSONField(default=dict)

    class Meta:
        abstract = True

    def set_extra_field(self, key, value):
        """Set a key-value pair in the extra_data JSON field."""
        if AllowedKey.objects.filter(key=key).exists():
            self.extra_data[key] = value
            self.save()
        else:
            raise ValueError(f"Key '{key}' is not allowed.")

    def get_extra_field(self, key):
        """Get a value from the extra_data JSON field."""
        return self.extra_data.get(key)

    def remove_extra_field(self, key):
        """Remove a key-value pair from the extra_data JSON field."""
        if key in self.extra_data:
            del self.extra_data[key]
            self.save()

    def validate_extra_data(self):
        allowed_keys = AllowedKey.objects.filter(
            model_name=self.__class__.__name__
        )
        for allowed_key in allowed_keys:
            if allowed_key.key not in self.extra_data:
                raise ValueError(f"Missing allowed key: {allowed_key.key}")

            value = self.extra_data[allowed_key.key]
            if not self.validate_value_type(value, allowed_key.value_type):
                raise ValueError(
                    f"Invalid type for key '{allowed_key.key}': expected {allowed_key.value_type}, got {type(value).__name__}"
                )

    def validate_value_type(self, value, expected_type):
        if expected_type == AllowedKey.STRING:
            return isinstance(value, str)
        elif expected_type == AllowedKey.LIST:
            return isinstance(value, list)
        elif expected_type == AllowedKey.DICT:
            return isinstance(value, dict)
        elif expected_type == AllowedKey.NUMBER:
            return isinstance(value, (int, float))
        return False
