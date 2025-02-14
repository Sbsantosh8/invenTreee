from rest_framework.views import APIView


from rest_framework.response import Response
from django.db import transaction
from rest_framework import status
from lead_to_invoice.models import *
from .models import (
    Lead,
    Quotation,
    Invoice,
    NumberingSystemSettings,
    Notification,
    LeadToInvoice,
)
from django.core.exceptions import ValidationError
from datetime import datetime
import re
from django.utils import timezone
from .utils import ( generate_number)
from part.models import Part
from django.db import transaction
from .serializers import (
    LeadSerializer,
    QuotationSerializer,
    InvoiceSerializer,
    NumberingSystemSettingsSerializer,
    NotificationSerializer,
    LeadToInvoiceSerializer,
)



class CreateLeadView(APIView):
    queryset = Lead.objects.all()

    def post(self, request):
        data = request.data
        data["lead_number"] = generate_number("Lead")
        lead = Lead.objects.create(**data)
        return Response(
            {"message": "Lead created!", "lead_number": lead.lead_number},
            status=status.HTTP_201_CREATED,
        )

    def get(self, request):
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)


# class CreateInvoiceView(APIView):
#     queryset = Invoice.objects.all()

#     @transaction.atomic
#     def post(self, request):
#         data = request.data
        
#         # Get Quotation
#         try:
#             quotation = Quotation.objects.get(id=data['quotation_id'])  
#         except Quotation.DoesNotExist:
#             return Response({"error": "Quotation not found"}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Get Lead
#         try:
#             lead = Lead.objects.get(id=data['lead_id'])
#         except Lead.DoesNotExist:
#             return Response({"error": "Lead not found"}, status=status.HTTP_400_BAD_REQUEST)

#         # Generate invoice number
#         data['invoice_number'] = generate_number('Invoice')
#         print("data['invoice_number'] : ",data['invoice_number'])
        
#         # Try creating the invoice
#         try:
#             # Create the Invoice object
#             invoice = Invoice.objects.create(quotation=quotation, **data)

#             if invoice.status == 'paid':
#                 # Delete any existing invoices with the status 'partially_paid' or 'unpaid' for the same quotation
#                 Invoice.objects.filter(
#                     quotation=quotation,
#                     status__in=['partially_paid', 'unpaid']
#                 ).delete()

#             elif invoice.status == 'partially_paid':
#                 # Delete any existing invoices with the status 'unpaid' for the same quotation
#                 Invoice.objects.filter(
#                     quotation=quotation,
#                     status='unpaid'
#                 ).delete()    
           
            
           
#         except ValidationError as e:
#             # Catch the validation error and return it in the response
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Serialize the invoice object
#         serializer = InvoiceSerializer(invoice)
        
        
#         # Return the serialized data in the response
#         return Response({"message": "Invoice created!", "invoice": serializer.data}, status=status.HTTP_201_CREATED)


 
#     def get(self, request):
#         invoices = Invoice.objects.all()
#         serializer = InvoiceSerializer(invoices, many=True)
#         return Response(serializer.data)
      

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db import transaction
# from rest_framework import status
# from lead_to_invoice.models import Quotation, Lead, Invoice
# from .serializers import InvoiceSerializer
# from django.core.exceptions import ValidationError
# from datetime import datetime
# import pytz
# from django.utils import timezone
# from .utils import generate_number

# class CreateInvoiceView(APIView):
#     queryset = Invoice.objects.all()

#     @transaction.atomic
#     def post(self, request):
#         data = request.data

#         # Get Quotation
#         try:
#             quotation = Quotation.objects.get(id=data['quotation_id'])
#         except Quotation.DoesNotExist:
#             return Response({"error": "Quotation not found"}, status=status.HTTP_400_BAD_REQUEST)

#         # Get Lead
#         try:
#             lead = Lead.objects.get(id=data['lead_id'])
#         except Lead.DoesNotExist:
#             return Response({"error": "Lead not found"}, status=status.HTTP_400_BAD_REQUEST)

#         # Generate invoice number
#         data['invoice_number'] = generate_number('Invoice')
#         print("data['invoice_number']:", data['invoice_number'])

#         # Parse due_date
#         if 'due_date' in data:
#             try:
#                 data['due_date'] = datetime.strptime(data['due_date'], "%Y-%m-%dT%H:%M:%SZ")
#                 data['due_date'] = timezone.make_aware(data['due_date'], timezone=pytz.UTC)
#             except ValueError:
#                 return Response({"error": "Invalid due_date format"}, status=status.HTTP_400_BAD_REQUEST)

#         # Remove items field if it exists
#         data.pop('items', None)

#         # Try creating the invoice
#         try:
#             # Create the Invoice object
#             invoice = Invoice.objects.create(quotation=quotation, lead=lead, **data)

#             if invoice.status == 'paid':
#                 # Delete any existing invoices with the status 'partially_paid' or 'unpaid' for the same quotation
#                 Invoice.objects.filter(
#                     quotation=quotation,
#                     status__in=['partially_paid', 'unpaid']
#                 ).delete()

#             elif invoice.status == 'partially_paid':
#                 # Delete any existing invoices with the status 'unpaid' for the same quotation
#                 Invoice.objects.filter(
#                     quotation=quotation,
#                     status='unpaid'
#                 ).delete()

#         except ValidationError as e:
#             # Catch the validation error and return it in the response
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#         # Serialize the invoice object
#         serializer = InvoiceSerializer(invoice)

#         # Return the serialized data in the response
#         return Response({"message": "Invoice created!", "invoice": serializer.data}, status=status.HTTP_201_CREATED)

#     def get(self, request):
#         invoices = Invoice.objects.all()
#         serializer = InvoiceSerializer(invoices, many=True)
#         return Response(serializer.data)


from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status
from lead_to_invoice.models import Quotation, Lead, Invoice
from .serializers import InvoiceSerializer
from django.core.exceptions import ValidationError
from datetime import datetime
import pytz
from django.utils import timezone
from .utils import generate_number

class CreateInvoiceView(APIView):
    queryset = Invoice.objects.all()

    @transaction.atomic
    def post(self, request):
        data = request.data

        # Get Quotation
        try:
            quotation = Quotation.objects.get(id=data['quotation_id'])
        except Quotation.DoesNotExist:
            return Response({"error": "Quotation not found"}, status=status.HTTP_400_BAD_REQUEST)

        # Get Lead
        try:
            lead = Lead.objects.get(id=data['lead_id'])
        except Lead.DoesNotExist:
            return Response({"error": "Lead not found"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate invoice number
        data['invoice_number'] = generate_number('Invoice')

        # Parse due_date in dd-mm-yyyy format
        if 'due_date' in data:
            try:
                data['due_date'] = datetime.strptime(data['due_date'], "%d-%m-%Y")
                data['due_date'] = timezone.make_aware(data['due_date'], timezone=pytz.UTC)
            except ValueError:
                return Response({"error": "Invalid due_date format. Use dd-mm-yyyy"}, status=status.HTTP_400_BAD_REQUEST)

        # Remove items field if it exists
        data.pop('items', None)

        # Try creating the invoice
        try:
            invoice = Invoice.objects.create(quotation=quotation, lead=lead, **data)

            if invoice.status == 'paid':
                Invoice.objects.filter(
                    quotation=quotation,
                    status__in=['partially_paid', 'unpaid']
                ).delete()

            elif invoice.status == 'partially_paid':
                Invoice.objects.filter(
                    quotation=quotation,
                    status='unpaid'
                ).delete()

        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = InvoiceSerializer(invoice)
        return Response({"message": "Invoice created!", "invoice": serializer.data}, status=status.HTTP_201_CREATED)

    def get(self, request):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)




# class CreateQuotationView(APIView):
#     """API view for creating and retrieving notifications.

#     Handles POST requests to create new notifications and GET requests to retrieve all notifications.
#     """
    
#     @transaction.atomic
#     def post(self, request):
#         data = request.data
#         parent_quotation_id = data.get("parent_quotation_id")

#         # Check if lead_id is present in the request data
#         lead_id = data.get("lead_id")
#         if not lead_id:
#             return Response(
#                 {"error": "lead_id is required"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             lead = Lead.objects.get(id=lead_id)
#             print("lead_id :", lead.id)
#         except Lead.DoesNotExist:
#             return Response(
#                 {"error": "Lead not found"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         # Validate items
#         items = data.get("items")
#         if not isinstance(items, list) or not items:
#             return Response(
#                 {"error": "Items must be a non-empty list"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         # Validate and process items
#         items.sort(key=lambda x: x.get("item_name", ""))
#         for item in items:
#             part_id = item.get("part_id")
#             if not part_id:
#                 return Response(
#                     {"error": "Each item must have a part_id"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#             try:
#                 part = Part.objects.get(id=part_id)
#             except Part.DoesNotExist:
#                 return Response(
#                     {"error": f"Part with ID {part_id} not found"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#             item["part_id"] = part.id

#         # Process discount and tax
#         discount = data.get("discount", 0)
#         tax = data.get("tax", 0)

#         try:
#             discount = float(discount)
#             tax = float(tax)
#         except ValueError:
#             return Response(
#                 {"error": "Discount and tax must be valid numbers"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         # Calculate total amount
#         total_amount = 0
#         for item in items:
#             try:
#                 item["total"] = item["quantity"] * item["price"]
#                 total_amount += item["total"]
#             except KeyError:
#                 return Response(
#                     {"error": "Each item must have quantity and price"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#         # Apply discount and tax
#         total_amount -= total_amount * (discount / 100)
#         total_amount += total_amount * (tax / 100)

#         # Generate quotation number and create quotation within the same atomic block
#         try:
#             with transaction.atomic():
#                 # Generate unique quotation number
#                 while True:
#                     data["quotation_number"] = generate_number("Quotation")
#                     if not Quotation.objects.filter(quotation_number=data["quotation_number"]).exists():
#                         break
#                 print("data[quotation_number] :", data["quotation_number"])

#                 # Main Quotation Revision Logic for incrementing
#                 original_quotation = None
#                 if parent_quotation_id:
#                     try:
#                         parentObj = Quotation.objects.get(id=parent_quotation_id)
#                         splitted_value = str(parentObj.quotation_number).split("-")
#                         splitVal = float(splitted_value[-1]) + 0.1
#                         base_quotation_number = (
#                             f"{splitted_value[-3]}-{splitted_value[-2]}-{splitVal:.1f}"
#                         )
#                         data["quotation_number"] = base_quotation_number

#                         if data["quotation_number"][-1] == "0":
#                             data["quotation_number"] = data["quotation_number"][0:-2]

#                     except Quotation.DoesNotExist:
#                         return Response(
#                             {"error": "Parent quotation not found"},
#                             status=status.HTTP_400_BAD_REQUEST,
#                         )

#                 # Create quotation
#                 quotation = Quotation.objects.create(
#                     lead=lead,
#                     quotation_number=data["quotation_number"],
#                     items=items,
#                     total_amount=total_amount,
#                     discount=discount,
#                     tax=tax,
#                     status=data.get("status", "draft"),
#                     original_quotation=original_quotation,
#                 )
#                 print("quotation_id :", quotation.id)
#                 print("quotation_number :", quotation.quotation_number)

#         except IntegrityError as e:
#             return Response(
#                 {"error": "Duplicate quotation number"}, status=status.HTTP_400_BAD_REQUEST
#             )
#         except Exception as e:
#             return Response(
#                 {"error": str(e)},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         return Response(
#             {
#                 "message": "Quotation created!",
#                 "quotation_id": quotation.id,
#                 "quotation_number": quotation.quotation_number,
#                 "items": quotation.items,
#                 "discount": f"{int(quotation.discount)}%",
#                 "tax": f"{int(quotation.tax)}%",
#                 "total_amount": quotation.total_amount,
#                 "status": quotation.status,
#                 "parent_quotation_id": parent_quotation_id,
#             },
#             status=status.HTTP_201_CREATED,
#         )




#     def get(self, request, quotation_id=None):
#         if quotation_id:
#             try:
#                 quotation = Quotation.objects.get(id=quotation_id)
#                 return Response(QuotationSerializer(quotation).data)
#             except Quotation.DoesNotExist:
#                 return Response(
#                     {"error": "Quotation not found"},
#                     status=status.HTTP_404_NOT_FOUND,
#                 )

#         quotations = Quotation.objects.all()
#         return Response(QuotationSerializer(quotations, many=True).data)

class CreateQuotationView(APIView):
    """API view for creating and retrieving notifications.

    Handles POST requests to create new notifications and GET requests to retrieve all notifications.
    """
    
    @transaction.atomic
    def post(self, request):
        data = request.data
        parent_quotation_id = data.get("parent_quotation_id")

        # Check if lead_id is present in the request data
        lead_id = data.get("lead_id")
        if not lead_id:
            return Response(
                {"error": "lead_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            lead = Lead.objects.get(id=lead_id)
            print("lead_id :", lead.id)
        except Lead.DoesNotExist:
            return Response(
                {"error": "Lead not found"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Validate items
        items = data.get("items")
        if not isinstance(items, list) or not items:
            return Response(
                {"error": "Items must be a non-empty list"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validate and process items
        items.sort(key=lambda x: x.get("item_name", ""))
        for item in items:
            part_id = item.get("part_id")
            if not part_id:
                return Response(
                    {"error": "Each item must have a part_id"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            try:
                part = Part.objects.get(id=part_id)
            except Part.DoesNotExist:
                return Response(
                    {"error": f"Part with ID {part_id} not found"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            item["part_id"] = part.id

        # Process discount and tax
        discount = data.get("discount", 0)
        tax = data.get("tax", 0)

        try:
            discount = float(discount)
            tax = float(tax)
        except ValueError:
            return Response(
                {"error": "Discount and tax must be valid numbers"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Calculate total amount
        total_amount = 0
        for item in items:
            try:
                item["total"] = item["quantity"] * item["price"]
                total_amount += item["total"]
            except KeyError:
                return Response(
                    {"error": "Each item must have quantity and price"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        # Apply discount and tax
        total_amount -= total_amount * (discount / 100)
        total_amount += total_amount * (tax / 100)

        with transaction.atomic():
       
            if parent_quotation_id:
                try:
                    parent_quotation = Quotation.objects.get(id=parent_quotation_id)
           
                    base_quotation = parent_quotation
                    while base_quotation.original_quotation:
                        base_quotation = base_quotation.original_quotation
           
                    all_revisions = Quotation.objects.filter(
                        quotation_number__startswith=base_quotation.quotation_number + '.'
                    ).order_by('-quotation_number')
           
                    highest_revision = 0
                    for revision in all_revisions:
                        try:
                            revision_num = int(revision.quotation_number.split('.')[-1])
                            highest_revision = max(highest_revision, revision_num)
                        except (ValueError, IndexError):
                            continue
           
                    next_revision = highest_revision + 1
                    data["quotation_number"] = f"{base_quotation.quotation_number}.{next_revision}"
                    original_quotation = base_quotation
           
                except Quotation.DoesNotExist:
                    return Response(
                        {"error": "Original quotation not found"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                current_year = timezone.now().year
                last_quotation = (
                    Quotation.objects.filter(
                        quotation_number__regex=r'^QN-\d+-\d+$',  
                        created_at__year=current_year
                    )
                    .order_by('-quotation_number')
                    .first()
                )
       
                if last_quotation:
                    match = re.search(r'QN-(\d+)-\d+$', last_quotation.quotation_number)
                    if match:
                        last_number = int(match.group(1))
                        next_number = last_number + 1
                    else:
                        next_number = 1
                else:
                    next_number = 1
       
                data["quotation_number"] = f"QN-{next_number:03d}-{current_year}"
                original_quotation = None
 
            quotation = Quotation.objects.create(
                lead=lead,
                quotation_number=data["quotation_number"],
                items=items,
                total_amount=total_amount,
                discount=discount,
                tax=tax,
                status=data.get("status", "draft"),
                original_quotation=original_quotation,
            )
 
            return Response(
                {
                    "message": "Quotation created!",
                    "quotation_id": quotation.id,
                    "quotation_number": quotation.quotation_number,
                    "items": quotation.items,
                    "discount": f"{int(quotation.discount)}%",
                    "tax": f"{int(quotation.tax)}%",
                    "total_amount": quotation.total_amount,
                    "status": quotation.status,
                    "parent_quotation_id": parent_quotation_id,
                    
                },
                status=status.HTTP_201_CREATED,
            )




    def get(self, request, quotation_id=None):
        if quotation_id:
            try:
                quotation = Quotation.objects.get(id=quotation_id)
                return Response(QuotationSerializer(quotation).data)
            except Quotation.DoesNotExist:
                return Response(
                    {"error": "Quotation not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

        quotations = Quotation.objects.all()
        return Response(QuotationSerializer(quotations, many=True).data)


class NumberingSystemSettingsAPI(APIView):
    queryset = NumberingSystemSettings.objects.all()

    def get(self, request):
        settings = NumberingSystemSettings.objects.all()
        serializer = NumberingSystemSettingsSerializer(settings, many=True)
        return Response(serializer.data)


    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from lead_to_invoice.models import LeadToInvoice
from .serializers import LeadToInvoiceSerializer

class LeadToInvoiceView(APIView):
    queryset = LeadToInvoice.objects.all()

    def get(self, request):
        lead_to_invoices = LeadToInvoice.objects.all()
        serializer = LeadToInvoiceSerializer(lead_to_invoices, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = LeadToInvoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NotificationAPI(APIView):
    """API view for creating and retrieving notifications.

    Handles POST requests to create new notifications and GET requests to retrieve all notifications.
"""
    
    queryset = Notification.objects.all()

    def post(self, request):
        data = request.data

        # Handle 'lead' field
        lead_id = data.get("lead")
        if lead_id:
            try:
                lead_instance = Lead.objects.get(id=lead_id)
                data["lead"] = lead_instance
            except Lead.DoesNotExist:
                return Response(
                    {"message": "Lead not found!"}, status=status.HTTP_404_NOT_FOUND
                )

        quotation_id = data.get("quotation")
        if quotation_id:
            try:
                quotation_instance = Quotation.objects.get(id=quotation_id)
                data["quotation"] = quotation_instance
            except Quotation.DoesNotExist:
                return Response(
                    {"message": "Quotation not found!"},
                    status=status.HTTP_404_NOT_FOUND,
                )

        try:
            notification = Notification.objects.create(**data)
            return Response(
                {
                    "message": "Notification created!",
                    "notification_id": notification.id,
                },
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)


    
