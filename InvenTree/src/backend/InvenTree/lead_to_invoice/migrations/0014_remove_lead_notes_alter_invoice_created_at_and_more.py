# Generated by Django 5.1.6 on 2025-02-14 10:08

import django.core.validators
import django.utils.timezone
import lead_to_invoice.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lead_to_invoice", "0013_invoice_total_amount_alter_invoice_lead"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lead",
            name="notes",
        ),
        migrations.AlterField(
            model_name="invoice",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="lead",
            name="address",
            field=models.TextField(
                validators=[
                    django.core.validators.MinLengthValidator(
                        10, "Address must be at least 10 characters long"
                    )
                ]
            ),
        ),
        migrations.AlterField(
            model_name="lead",
            name="email",
            field=models.EmailField(
                help_text="Enter a valid Gmail address",
                max_length=254,
                validators=[
                    django.core.validators.EmailValidator(),
                    lead_to_invoice.models.validate_gmail,
                ],
            ),
        ),
        migrations.AlterField(
            model_name="lead",
            name="name",
            field=models.CharField(
                help_text="Enter only alphabetical characters and spaces",
                max_length=255,
                validators=[lead_to_invoice.models.validate_name],
            ),
        ),
        migrations.AlterField(
            model_name="lead",
            name="phone",
            field=models.CharField(
                help_text="Enter at least 10 digits",
                max_length=15,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be between 10 and 15 digits",
                        regex="^\\d{10,15}$",
                    ),
                    django.core.validators.MinLengthValidator(10),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="lead",
            name="source",
            field=models.CharField(
                max_length=255,
                validators=[
                    django.core.validators.MinLengthValidator(
                        2, "Source must be at least 2 characters long"
                    )
                ],
            ),
        ),
        migrations.AddIndex(
            model_name="lead",
            index=models.Index(fields=["phone"], name="lead_to_inv_phone_3b9f42_idx"),
        ),
        migrations.AddIndex(
            model_name="lead",
            index=models.Index(fields=["status"], name="lead_to_inv_status_b7e207_idx"),
        ),
    ]
