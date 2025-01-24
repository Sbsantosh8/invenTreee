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
        fields = "__all__"


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
from decimal import Decimal

class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = [
            "id",
            "lead",
            "items",
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
    amount_due = serializers.SerializerMethodField()
    class Meta:
        model = Invoice
        fields = "__all__"

    


    def get_amount_due(self, obj):
    # Access the associated Quotation and calculate amount_due
     if obj.quotation:
        total_amount = obj.quotation.total_amount
        paid_amount = Decimal(obj.paid_amount)  # Convert paid_amount to Decimal if it's a string
        return total_amount - paid_amount
     return None


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
