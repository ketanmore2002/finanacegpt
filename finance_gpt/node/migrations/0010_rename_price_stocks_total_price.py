# Generated by Django 4.1.1 on 2024-03-29 19:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("node", "0009_alter_stocks_user_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="stocks",
            old_name="price",
            new_name="total_price",
        ),
    ]
