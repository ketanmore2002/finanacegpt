# Generated by Django 4.1.1 on 2024-04-06 23:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("node", "0012_messages_type_alter_transactions_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stocks",
            name="user_id",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
