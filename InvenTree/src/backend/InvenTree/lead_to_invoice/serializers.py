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






      
from pytz import timezone as pytz_timezone
from datetime import datetime
from dateutil.parser import parse as dateutil_parse

class InvoiceSerializer(serializers.ModelSerializer):
    quotation_number = serializers.SerializerMethodField()
    lead_id = serializers.ReadOnlyField(source='quotation.lead.id')
    created_at = serializers.SerializerMethodField()
    due_date = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ['id', 'quotation', 'quotation_number', 'invoice_number', 'total_amount', 'paid_amount', 'amount_due', 'status', 'created_at', 'lead_id', 'due_date']

    def get_quotation_number(self, obj):
        return obj.quotation.quotation_number if obj.quotation else None

    def get_created_at(self, obj):
        local_tz = pytz_timezone('Asia/Kolkata')
        local_time = obj.created_at.astimezone(local_tz)
        return local_time.strftime("%d-%m-%Y ")

    def get_due_date(self, obj):
        if obj.due_date:
            try:
                # Ensure obj.due_date is a string before parsing
                due_date_str = str(obj.due_date)
                # Parse the due_date string to a datetime object
                due_date = dateutil_parse(due_date_str)
                local_tz = pytz_timezone('Asia/Kolkata')
                local_time = due_date.astimezone(local_tz)
                return local_time.strftime("%d-%m-%Y ")
            except (ValueError, TypeError):
                return obj.due_date  # Return the original value if parsing fails
        return None



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



class LeadToInvoiceSerializer(serializers.ModelSerializer):
    lead = LeadSerializer()  
    quotation = QuotationSerializer(
        required=False
    )  
    invoice = InvoiceSerializer(
        required=False
    ) 

    class Meta:
        model = LeadToInvoice
        fields = "__all__"

  
    def validate(self, data):
        if not data.get("quotation") and not data.get("invoice"):
            raise serializers.ValidationError(
                "Either Quotation or Invoice must be provided."
            )
        return data
