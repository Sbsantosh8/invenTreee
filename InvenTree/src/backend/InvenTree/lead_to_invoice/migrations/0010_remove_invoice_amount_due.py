# Generated by Django 4.2.17 on 2025-01-24 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lead_to_invoice", "0009_quotation_items"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="invoice",
            name="amount_due",
        ),
    ]
