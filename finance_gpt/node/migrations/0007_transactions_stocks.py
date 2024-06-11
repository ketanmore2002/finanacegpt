# Generated by Django 4.1.1 on 2024-03-29 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("node", "0006_remove_messages_last_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transactions",
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
                ("uuid", models.UUIDField(blank=True, default=uuid.uuid4, null=True)),
                ("date_field", models.DateField(auto_now_add=True, null=True)),
                ("time_field", models.TimeField(auto_now_add=True, null=True)),
                ("ticker", models.CharField(blank=True, max_length=50, null=True)),
                ("quantity", models.IntegerField(blank=True, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("Sell", "Sell"), ("Purchase", "Purchase")],
                        max_length=20,
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Transactions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="stocks",
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
                ("uuid", models.UUIDField(blank=True, default=uuid.uuid4, null=True)),
                ("date_field", models.DateField(auto_now_add=True, null=True)),
                ("time_field", models.TimeField(auto_now_add=True, null=True)),
                ("ticker", models.CharField(blank=True, max_length=50, null=True)),
                ("quantity", models.IntegerField(blank=True, null=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stocks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
