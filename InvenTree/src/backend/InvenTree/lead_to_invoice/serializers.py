from rest_framework import serializers
from .models import (
    Lead,
    Quotation,
    Invoice,
    NumberingSystemSettings,
    Notification,
    LeadToInvoice,
)


# Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "status",
            "created_at",
            "updated_at",
        ]  # Explicit fields


# Quotation Serializer
# class QuotationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Quotation
#         fields = [
#             "id",  # Ensure that the id field is explicitly included
#             "lead",
#             "total_amount",
#             "discount",
#             "tax",
#             "status",
#             "quotation_number",
#         ]


# class QuotationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Quotation
#         fields = [
#             "id",  # Explicitly include the 'id' field
#         ]


from rest_framework import serializers
from .models import Quotation


class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = [
            "id",
            "lead",
            "total_amount",
            "discount",
            "tax",
            "status",
            "quotation_number",
        ]

    def validate_quotation_number(self, value):
        """
        Ensure that the quotation number is unique.
        """
        if Quotation.objects.filter(quotation_number=value).exists():
            raise serializers.ValidationError("Quotation number must be unique.")
        return value


# Invoice Serializer
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = [
            "id",
            "quotation",
            "invoice_number",
            "amount_due",
            "status",
            "created_at",
        ]


# NumberingSystemSettings Serializer
class NumberingSystemSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberingSystemSettings
        fields = [
            "type",
            "prefix",
            "suffix",
            "current_number",
            "increment_step",
            "reset_cycle",
        ]


# Notification Serializer
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "type",
            "recipient",
            "status",
            "message",
            "timestamp",
            "lead",
            "quotation",
            "invoice",
        ]


# LeadToInvoice Serializer (with nested serializers)
class LeadToInvoiceSerializer(serializers.ModelSerializer):
    lead = LeadSerializer()  # Nested Lead serializer
    quotation = QuotationSerializer(
        required=False
    )  # Nested Quotation serializer if available
    invoice = InvoiceSerializer(
        required=False
    )  # Nested Invoice serializer if available

    class Meta:
        model = LeadToInvoice
        fields = "__all__"

    # Custom validation to ensure either Quotation or Invoice is provided
    def validate(self, data):
        if not data.get("quotation") and not data.get("invoice"):
            raise serializers.ValidationError(
                "Either Quotation or Invoice must be provided."
            )
        return data
