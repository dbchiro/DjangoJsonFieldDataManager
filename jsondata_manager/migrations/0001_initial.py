# Generated by Django 4.2.16 on 2024-10-01 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AllowedKey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model_name", models.CharField(max_length=100)),
                ("key", models.CharField(max_length=100, unique=True)),
                (
                    "value_type",
                    models.CharField(
                        choices=[
                            ("string", "String"),
                            ("number", "Number"),
                            ("list", "List"),
                            ("dict", "Dict"),
                        ],
                        max_length=10,
                    ),
                ),
                ("hidden", models.BooleanField(default=False)),
            ],
        ),
    ]
