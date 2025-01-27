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


# # Invoice Serializer
# class InvoiceSerializer(serializers.ModelSerializer):
#     amount_due = serializers.SerializerMethodField()
#     class Meta:
#         model = Invoice
#         fields = "__all__"


#     # def create(self, validated_data):
#     #     # Extract quotation_id and get the Quotation object
#     #     quotation_id = validated_data.pop('quotation_id')
#     #     try:
#     #         quotation = Quotation.objects.get(id=quotation_id)
#     #     except Quotation.DoesNotExist:
#     #         raise serializers.ValidationError({'quotation': 'Quotation not found'})
        
#     #     # Create invoice with the Quotation object
#     #     validated_data['quotation'] = quotation
#     #     return Invoice.objects.create(**validated_data)    

    


#     # def get_amount_due(self, obj):
#     # # Access the associated Quotation and calculate amount_due
#     #  print("obj.....................",obj)
#     #  if obj.quotation:
#     #     print("inside get_amount_due ............",obj.quotation)
#     #     total_amount = obj.quotation.total_amount
#     #     print("total_amount.......",total_amount)

#     #     paid_amount = Decimal(obj.paid_amount)  # Convert paid_amount to Decimal if it's a string
#     #     print("paid_amount.......",paid_amount)
#     #     print("amount_due.......",total_amount - paid_amount)
#     #     return total_amount - paid_amount
#     #  return None


#     def get_amount_due(self, obj):
#         if obj.quotation:
#             total_amount = obj.quotation.total_amount
#             paid_amount = Decimal(obj.paid_amount)
#             amount_due = total_amount - paid_amount
           
#             return amount_due
#         return None


# class InvoiceSerializer(serializers.ModelSerializer):
#     amount_due = serializers.SerializerMethodField()  # Still useful for read-only serialization

#     class Meta:
#         model = Invoice
#         fields = "__all__"

#     def create(self, validated_data):
#         # Calculate amount_due and save it to the instance
#         quotation = validated_data.get("quotation")
#         paid_amount = validated_data.get("paid_amount", 0)

#         # Ensure quotation exists
#         if quotation:
#             total_amount = quotation.total_amount
#             validated_data["amount_due"] = total_amount - paid_amount
#         else:
#             raise serializers.ValidationError({"quotation": "Quotation is required to calculate amount_due"})

#         return super().create(validated_data)

#     # def update(self, instance, validated_data):
#     #     # Recalculate amount_due during updates
#     #     quotation = validated_data.get("quotation", instance.quotation)
#     #     paid_amount = validated_data.get("paid_amount", instance.paid_amount)

#     #     # Ensure quotation exists
#     #     if quotation:
#     #         total_amount = quotation.total_amount
#     #         instance.amount_due = total_amount - paid_amount

#     #     # Update other fields
#     #     for attr, value in validated_data.items():
#     #         setattr(instance, attr, value)

#     #     instance.save()
#     #     return instance
#     def update(self, instance, validated_data):
#     # Recalculate amount_due during updates
#         quotation = validated_data.get("quotation", instance.quotation)
#         paid_amount = validated_data.get("paid_amount", instance.paid_amount)

#     # Ensure quotation exists
#         if quotation:
#             total_amount = quotation.total_amount
#             instance.amount_due = total_amount - paid_amount

#     # Update other fields
#         for attr, value in validated_data.items():
#          if attr not in ['amount_due']:  # Don't overwrite the amount_due again
#             setattr(instance, attr, value)

#         instance.save()
#         return instance


#     def get_amount_due(self, obj):
#         # Optional: dynamic read-only calculation
#         if obj.quotation:
#             total_amount = obj.quotation.total_amount
#             paid_amount = Decimal(obj.paid_amount)
#             return total_amount - paid_amount
#         return None

# class InvoiceSerializer(serializers.ModelSerializer):
#     amount_due = serializers.SerializerMethodField()  # Dynamic amount_due calculation

#     class Meta:
#         model = Invoice
#         fields = "__all__"

#     def create(self, validated_data):
#         # Calculate amount_due during create
#         quotation = validated_data.get("quotation")
#         paid_amount = validated_data.get("paid_amount", Decimal("0.00"))  # Default to 0 if not provided

#         # Ensure quotation exists and get total amount from quotation
#         if quotation:
#             total_amount = quotation.total_amount
#             validated_data["amount_due"] = total_amount - paid_amount
#         else:
#             raise serializers.ValidationError({"quotation": "Quotation is required to calculate amount_due"})

#         return super().create(validated_data)
    
#     def update(self, instance, validated_data):
#     # Recalculate amount_due during updates
#         quotation = validated_data.get("quotation", instance.quotation)
#         paid_amount = validated_data.get("paid_amount", instance.paid_amount)

#     # Ensure quotation exists and get total amount from quotation
#         if quotation:
#             total_amount = quotation.total_amount
#             instance.amount_due = total_amount - paid_amount

#     # Update other fields
#         for attr, value in validated_data.items():
#             if attr not in ['amount_due']:  # Don't overwrite the amount_due again
#              setattr(instance, attr, value)

#         instance.save()
#         return instance


#     def get_amount_due(self, obj):
#         # Dynamic calculation of amount_due for read-only views
#         total_amount = obj.quotation.total_amount
#         paid_amount = obj.paid_amount
#         return total_amount - paid_amount

# from decimal import Decimal
# from rest_framework import serializers
# from .models import Invoice, Quotation

# class InvoiceSerializer(serializers.ModelSerializer):
#     amount_due = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

#     class Meta:
#         model = Invoice
#         fields = [
#             'id',
#             'invoice_number',
#             'quotation',
#             'total_amount',
#             'amount_due',
#             'paid_amount',
             
#             'status',
#             'created_at',
            
#         ]

   

    # def get_amount_due(self, obj):
    #     # Dynamic calculation of amount_due for read-only views
    #     print("inside get_amount_due : ",obj.amount_due)
    #     total_amount = obj.quotation.total_amount
    #     paid_amount = obj.paid_amount
    #     return total_amount - paid_amount



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
