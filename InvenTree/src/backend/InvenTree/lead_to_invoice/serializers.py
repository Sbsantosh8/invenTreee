from rest_framework import serializers
from .models import (
    Lead,
    Quotation,
    Invoice,
    NumberingSystemSettings,
    Notification,
    LeadToInvoice,
)



"""  Serializes all fields of the Lead model."""
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"



from rest_framework import serializers
from .models import Quotation
from decimal import Decimal
 
"""Serializer for Quotation models.

  Serializes Quotation model fields and validates quotation number uniqueness.
"""
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








class InvoiceSerializer(serializers.ModelSerializer):
    quotation_number = serializers.SerializerMethodField()
    class Meta:
        model = Invoice
        fields = ['id', 'quotation','quotation_number', 'invoice_number','total_amount','paid_amount', 'amount_due', 'status', 'created_at'] 


    def get_quotation_number(self, obj):
        # Accessing the 'quotation_number' field from the related 'Quotation' model
        return obj.quotation.quotation_number if obj.quotation else None
      


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
