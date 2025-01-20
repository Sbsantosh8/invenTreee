# # # from rest_framework.views import APIView
# # # from rest_framework.response import Response
# # # from rest_framework import status
# # # from .models import Lead, Quotation, Invoice, NumberingSystemSettings, Notification, LeadToInvoice
# # # from .serializers import LeadSerializer, QuotationSerializer, InvoiceSerializer, NumberingSystemSettingsSerializer, NotificationSerializer, LeadToInvoiceSerializer


# # # # Function to generate unique numbers based on the numbering system settings
# # # def generate_number(type):
# # #     settings = NumberingSystemSettings.objects.get(type=type)
# # #     current_number = settings.current_number
# # #     # Format the number using the prefix, current number, and suffix
# # #     new_number = f"{settings.prefix or ''}{current_number}{settings.suffix or ''}"
# # #     # Increment the current number based on the step
# # #     settings.current_number += settings.increment_step
# # #     settings.save()
# # #     return new_number


# # # class CreateLeadView(APIView):
# # #     queryset = Lead.objects.all()

# # #     def post(self, request):
# # #         data = request.data
# # #         # Assign a generated lead number
# # #         data['lead_number'] = generate_number('Lead')
# # #         # Create the lead record
# # #         lead = Lead.objects.create(**data)
# # #         return Response({"message": "Lead created!", "lead_number": lead.lead_number}, status=status.HTTP_201_CREATED)

# # #     def get(self, request):
# # #         leads = Lead.objects.all()
# # #         serializer = LeadSerializer(leads, many=True)
# # #         return Response(serializer.data)

# # # class CreateQuotationView(APIView):
# # #     queryset = Quotation.objects.all()
# # #     def post(self, request):
# # #         data = request.data
# # #         lead = Lead.objects.get(id=data['lead_id'])  # Retrieve the related lead
# # #         # Assign a generated quotation number
# # #         data['quotation_number'] = generate_number('Quotation')
# # #         # Create the quotation record
# # #         quotation = Quotation.objects.create(lead=lead, **data)
# # #         return Response({"message": "Quotation created!", "quotation_number": quotation.quotation_number}, status=status.HTTP_201_CREATED)

# # #     def get(self, request):
# # #         quotations = Quotation.objects.all()
# # #         serializer = QuotationSerializer(quotations, many=True)
# # #         return Response(serializer.data)

# # # class CreateInvoiceView(APIView):
# # #     queryset = Invoice.objects.all()
# # #     def post(self, request):
# # #         data = request.data
# # #         quotation = Quotation.objects.get(id=data['quotation_id'])  # Retrieve the related quotation
# # #         # Assign a generated invoice number
# # #         data['invoice_number'] = generate_number('Invoice')
# # #         # Create the invoice record
# # #         invoice = Invoice.objects.create(quotation=quotation, **data)
# # #         return Response({"message": "Invoice created!", "invoice_number": invoice.invoice_number}, status=status.HTTP_201_CREATED)

# # #     def get(self, request):
# # #         invoices = Invoice.objects.all()
# # #         serializer = InvoiceSerializer(invoices, many=True)
# # #         return Response(serializer.data)

# # # class NotificationAPI(APIView):
# # #     queryset = Notification.objects.all()
# # #     def get(self, request):
# # #         notifications = Notification.objects.all()
# # #         serializer = NotificationSerializer(notifications, many=True)
# # #         return Response(serializer.data)

# # # class LeadToInvoiceView(APIView):
# # #     queryset = LeadToInvoice.objects.all()

# # #     def get(self, request):
# # #         # Gather the data
# # #         leads = Lead.objects.all()  # Adjust query as needed
# # #         quotations = Quotation.objects.filter(lead__in=leads)
# # #         invoices = Invoice.objects.filter(quotation__in=quotations)

# # #         data = []
# # #         for invoice in invoices:
# # #             data.append({
# # #                 'lead': invoice.quotation.lead.name,
# # #                 'quotation_number': invoice.quotation.quotation_number,
# # #                 'invoice_number': invoice.invoice_number,
# # #                 'amount_due': invoice.amount_due,
# # #                 'status': invoice.status,
# # #             })

# # #         return Response(data)

# # #     def post(self, request):
# # #         data = request.data

# # #         # Validate and create the LeadToInvoice record
# # #         serializer = LeadToInvoiceSerializer(data=data)
# # #         if serializer.is_valid():
# # #             lead_to_invoice = serializer.save()  # Save the new LeadToInvoice instance
# # #             return Response({"message": "Lead to Invoice record created!", "id": lead_to_invoice.id}, status=status.HTTP_201_CREATED)
# # #         else:
# # #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # class NumberingSystemSettingsAPI(APIView):
# # #     queryset = NumberingSystemSettings.objects.all()
# # #     def get(self, request):
# # #         settings = NumberingSystemSettings.objects.all()
# # #         serializer = NumberingSystemSettingsSerializer(settings, many=True)
# # #         return Response(serializer.data)

# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status
# # from .models import (
# #     Lead,
# #     Quotation,
# #     Invoice,
# #     NumberingSystemSettings,
# #     Notification,
# #     LeadToInvoice,
# # )
# # from .serializers import (
# #     LeadSerializer,
# #     QuotationSerializer,
# #     InvoiceSerializer,
# #     NumberingSystemSettingsSerializer,
# #     NotificationSerializer,
# #     LeadToInvoiceSerializer,
# # )


# # # Function to generate unique numbers based on the numbering system settings
# # def generate_number(type):
# #     settings = NumberingSystemSettings.objects.get(type=type)
# #     current_number = settings.current_number
# #     new_number = f"{settings.prefix or ''}{current_number}{settings.suffix or ''}"
# #     settings.current_number += settings.increment_step
# #     settings.save()
# #     return new_number


# # # from django.views.decorators.csrf import csrf_exempt
# # # from django.utils.decorators import method_decorator


# # # @method_decorator(csrf_exempt, name="dispatch")
# # # class CreateLeadView(APIView):
# # #     queryset = Lead.objects.all()

# # #     def post(self, request):
# # #         data = request.data
# # #         data["lead_number"] = generate_number("Lead")
# # #         lead = Lead.objects.create(**data)
# # #         return Response(
# # #             {"message": "Lead created!", "lead_number": lead.lead_number},
# # #             status=status.HTTP_201_CREATED,
# # #         )

# # #     def get(self, request):
# # #         leads = Lead.objects.all()
# # #         serializer = LeadSerializer(leads, many=True)
# # #         return Response(serializer.data)

# # import logging
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator
# # from .models import Lead
# # from .serializers import LeadSerializer

# # # Setting up logger for better error tracking
# # logger = logging.getLogger(__name__)


# # # CSRF exemption for the view
# # @method_decorator(csrf_exempt, name="dispatch")
# # class CreateLeadView(APIView):
# #     queryset = Lead.objects.all()

# #     def generate_number(self, prefix):
# #         """
# #         Function to generate a unique lead number (e.g., Lead-001)
# #         Adjust this logic based on your needs.
# #         """
# #         from random import randint

# #         return f"{prefix}-{randint(100, 999)}"

# #     def post(self, request):
# #         """
# #         Handle the POST request to create a new lead.
# #         """
# #         try:
# #             # Get the incoming request data
# #             data = request.data

# #             # Ensure the required fields are provided
# #             required_fields = [
# #                 "name",
# #                 "email",
# #                 "phone",
# #             ]  # Add your required fields here
# #             for field in required_fields:
# #                 if field not in data:
# #                     return Response(
# #                         {"error": f"Missing required field: {field}"},
# #                         status=status.HTTP_400_BAD_REQUEST,
# #                     )

# #             # Generate lead number
# #             data["lead_number"] = self.generate_number("Lead")

# #             # Create the new Lead object
# #             lead = Lead.objects.create(**data)

# #             # Log the successful lead creation
# #             logger.info(f"Lead created: {lead.lead_number}, User ID: {request.user.id}")

# #             return Response(
# #                 {"message": "Lead created!", "lead_number": lead.lead_number},
# #                 status=status.HTTP_201_CREATED,
# #             )

# #         except Exception as e:
# #             # Log the error details
# #             logger.error(f"Error creating lead: {e}")

# #             return Response(
# #                 {"error": "An error occurred while creating the lead."},
# #                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
# #             )

# #     def get(self, request):
# #         """
# #         Handle the GET request to retrieve all leads.
# #         """
# #         try:
# #             # Retrieve all leads from the database
# #             leads = Lead.objects.all()

# #             # Serialize the data using LeadSerializer
# #             serializer = LeadSerializer(leads, many=True)

# #             # Return the serialized data as a response
# #             return Response(serializer.data)

# #         except Exception as e:
# #             # Log the error details
# #             logger.error(f"Error fetching leads: {e}")

# #             return Response(
# #                 {"error": "An error occurred while fetching the leads."},
# #                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
# #             )


# # # from django.views.decorators.csrf import csrf_exempt
# # # from django.utils.decorators import method_decorator


# # # @method_decorator(csrf_exempt, name="dispatch")
# # # class CreateQuotationView(APIView):
# # #     queryset = Quotation.objects.all()

# # #     def post(self, request):
# # #         data = request.data
# # #         try:
# # #             lead = Lead.objects.get(id=data["lead_id"])
# # #         except Lead.DoesNotExist:
# # #             return Response(
# # #                 {"error": "Lead not found"}, status=status.HTTP_400_BAD_REQUEST
# # #             )

# # #         data["quotation_number"] = generate_number("Quotation")
# # #         quotation = Quotation.objects.create(lead=lead, **data)
# # #         return Response(
# # #             {
# # #                 "message": "Quotation created!",
# # #                 "quotation_number": quotation.quotation_number,
# # #             },
# # #             status=status.HTTP_201_CREATED,
# # #         )

# # #     def get(self, request):
# # #         quotations = Quotation.objects.all()
# # #         serializer = QuotationSerializer(quotations, many=True)
# # #         return Response(serializer.data)

# # from rest_framework.exceptions import ValidationError


# # @method_decorator(csrf_exempt, name="dispatch")
# # class CreateQuotationView(APIView):
# #     queryset = Quotation.objects.all()

# #     def post(self, request):
# #         data = request.data

# #         # Check if 'lead_id' is in the request data
# #         if "lead" not in data:
# #             raise ValidationError({"error": "lead_id is required"})

# #         try:
# #             # Try to get the Lead object
# #             lead = Lead.objects.get(id=data["lead_id"])
# #         except Lead.DoesNotExist:
# #             return Response(
# #                 {"error": "Lead not found"}, status=status.HTTP_400_BAD_REQUEST
# #             )

# #         # Generate a quotation number
# #         data["quotation_number"] = generate_number("Quotation")

# #         # Create a new quotation
# #         quotation = Quotation.objects.create(lead=lead, **data)

# #         return Response(
# #             {
# #                 "message": "Quotation created!",
# #                 "quotation_number": quotation.quotation_number,
# #             },
# #             status=status.HTTP_201_CREATED,
# #         )

# #     def get(self, request):
# #         quotations = Quotation.objects.all()
# #         serializer = QuotationSerializer(quotations, many=True)
# #         return Response(serializer.data)


# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator


# # @method_decorator(csrf_exempt, name="dispatch")
# # class CreateInvoiceView(APIView):
# #     queryset = Invoice.objects.all()

# #     def post(self, request):
# #         data = request.data
# #         try:
# #             quotation = Quotation.objects.get(id=data["quotation_id"])
# #         except Quotation.DoesNotExist:
# #             return Response(
# #                 {"error": "Quotation not found"}, status=status.HTTP_400_BAD_REQUEST
# #             )

# #         data["invoice_number"] = generate_number("Invoice")
# #         invoice = Invoice.objects.create(quotation=quotation, **data)
# #         return Response(
# #             {"message": "Invoice created!", "invoice_number": invoice.invoice_number},
# #             status=status.HTTP_201_CREATED,
# #         )

# #     def get(self, request):
# #         invoices = Invoice.objects.all()
# #         serializer = InvoiceSerializer(invoices, many=True)
# #         return Response(serializer.data)


# # # class NotificationAPI(APIView):
# # #     queryset = Notification.objects.all()

# # #     def post(self, request):
# # #         data = request.data
# # #         notification = Notification.objects.create(**data)
# # #         return Response({"message": "Notification created!", "notification_id": notification.id}, status=status.HTTP_201_CREATED)

# # #     def get(self, request):
# # #         notifications = Notification.objects.all()
# # #         serializer = NotificationSerializer(notifications, many=True)
# # #         return Response(serializer.data)

# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator


# # @method_decorator(csrf_exempt, name="dispatch")
# # class LeadToInvoiceView(APIView):
# #     queryset = LeadToInvoice.objects.all()

# #     def get(self, request):
# #         leads = Lead.objects.all()
# #         quotations = Quotation.objects.filter(lead__in=leads)
# #         invoices = Invoice.objects.filter(quotation__in=quotations)

# #         data = []
# #         for invoice in invoices:
# #             data.append(
# #                 {
# #                     "lead": invoice.quotation.lead.name,
# #                     "quotation_number": invoice.quotation.quotation_number,
# #                     "invoice_number": invoice.invoice_number,
# #                     "amount_due": invoice.amount_due,
# #                     "status": invoice.status,
# #                 }
# #             )

# #         return Response(data)

# #     def post(self, request):
# #         data = request.data

# #         serializer = LeadToInvoiceSerializer(data=data)
# #         if serializer.is_valid():
# #             lead_to_invoice = serializer.save()
# #             return Response(
# #                 {
# #                     "message": "Lead to Invoice record created!",
# #                     "id": lead_to_invoice.id,
# #                 },
# #                 status=status.HTTP_201_CREATED,
# #             )
# #         else:
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator


# # @method_decorator(csrf_exempt, name="dispatch")
# # class NumberingSystemSettingsAPI(APIView):
# #     queryset = NumberingSystemSettings.objects.all()

# #     def get(self, request):
# #         settings = NumberingSystemSettings.objects.all()
# #         serializer = NumberingSystemSettingsSerializer(settings, many=True)
# #         return Response(serializer.data)


# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator


# # @method_decorator(csrf_exempt, name="dispatch")
# # class NotificationAPI(APIView):
# #     queryset = Notification.objects.all()

# #     def post(self, request):
# #         data = request.data

# #         # Handle 'lead' field
# #         lead_id = data.get("lead")
# #         if lead_id:
# #             try:
# #                 lead_instance = Lead.objects.get(id=lead_id)
# #                 data["lead"] = lead_instance
# #             except Lead.DoesNotExist:
# #                 return Response(
# #                     {"message": "Lead not found!"}, status=status.HTTP_404_NOT_FOUND
# #                 )

# #         quotation_id = data.get("quotation")
# #         if quotation_id:
# #             try:
# #                 quotation_instance = Quotation.objects.get(id=quotation_id)
# #                 data["quotation"] = quotation_instance
# #             except Quotation.DoesNotExist:
# #                 return Response(
# #                     {"message": "Quotation not found!"},
# #                     status=status.HTTP_404_NOT_FOUND,
# #                 )

# #         try:
# #             notification = Notification.objects.create(**data)
# #             return Response(
# #                 {
# #                     "message": "Notification created!",
# #                     "notification_id": notification.id,
# #                 },
# #                 status=status.HTTP_201_CREATED,
# #             )

# #         except Exception as e:
# #             return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# #     def get(self, request):
# #         notifications = Notification.objects.all()
# #         serializer = NotificationSerializer(notifications, many=True)
# #         return Response(serializer.data)


# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status
# # from .models import Lead, Quotation, Invoice, NumberingSystemSettings, Notification, LeadToInvoice
# # from .serializers import LeadSerializer, QuotationSerializer, InvoiceSerializer, NumberingSystemSettingsSerializer, NotificationSerializer, LeadToInvoiceSerializer


# # # Function to generate unique numbers based on the numbering system settings
# # def generate_number(type):
# #     settings = NumberingSystemSettings.objects.get(type=type)
# #     current_number = settings.current_number
# #     # Format the number using the prefix, current number, and suffix
# #     new_number = f"{settings.prefix or ''}{current_number}{settings.suffix or ''}"
# #     # Increment the current number based on the step
# #     settings.current_number += settings.increment_step
# #     settings.save()
# #     return new_number


# # class CreateLeadView(APIView):
# #     queryset = Lead.objects.all()

# #     def post(self, request):
# #         data = request.data
# #         # Assign a generated lead number
# #         data['lead_number'] = generate_number('Lead')
# #         # Create the lead record
# #         lead = Lead.objects.create(**data)
# #         return Response({"message": "Lead created!", "lead_number": lead.lead_number}, status=status.HTTP_201_CREATED)

# #     def get(self, request):
# #         leads = Lead.objects.all()
# #         serializer = LeadSerializer(leads, many=True)
# #         return Response(serializer.data)

# # class CreateQuotationView(APIView):
# #     queryset = Quotation.objects.all()
# #     def post(self, request):
# #         data = request.data
# #         lead = Lead.objects.get(id=data['lead_id'])  # Retrieve the related lead
# #         # Assign a generated quotation number
# #         data['quotation_number'] = generate_number('Quotation')
# #         # Create the quotation record
# #         quotation = Quotation.objects.create(lead=lead, **data)
# #         return Response({"message": "Quotation created!", "quotation_number": quotation.quotation_number}, status=status.HTTP_201_CREATED)

# #     def get(self, request):
# #         quotations = Quotation.objects.all()
# #         serializer = QuotationSerializer(quotations, many=True)
# #         return Response(serializer.data)

# # class CreateInvoiceView(APIView):
# #     queryset = Invoice.objects.all()
# #     def post(self, request):
# #         data = request.data
# #         quotation = Quotation.objects.get(id=data['quotation_id'])  # Retrieve the related quotation
# #         # Assign a generated invoice number
# #         data['invoice_number'] = generate_number('Invoice')
# #         # Create the invoice record
# #         invoice = Invoice.objects.create(quotation=quotation, **data)
# #         return Response({"message": "Invoice created!", "invoice_number": invoice.invoice_number}, status=status.HTTP_201_CREATED)

# #     def get(self, request):
# #         invoices = Invoice.objects.all()
# #         serializer = InvoiceSerializer(invoices, many=True)
# #         return Response(serializer.data)

# # class NotificationAPI(APIView):
# #     queryset = Notification.objects.all()
# #     def get(self, request):
# #         notifications = Notification.objects.all()
# #         serializer = NotificationSerializer(notifications, many=True)
# #         return Response(serializer.data)

# # class LeadToInvoiceView(APIView):
# #     queryset = LeadToInvoice.objects.all()

# #     def get(self, request):
# #         # Gather the data
# #         leads = Lead.objects.all()  # Adjust query as needed
# #         quotations = Quotation.objects.filter(lead__in=leads)
# #         invoices = Invoice.objects.filter(quotation__in=quotations)

# #         data = []
# #         for invoice in invoices:
# #             data.append({
# #                 'lead': invoice.quotation.lead.name,
# #                 'quotation_number': invoice.quotation.quotation_number,
# #                 'invoice_number': invoice.invoice_number,
# #                 'amount_due': invoice.amount_due,
# #                 'status': invoice.status,
# #             })

# #         return Response(data)

# #     def post(self, request):
# #         data = request.data

# #         # Validate and create the LeadToInvoice record
# #         serializer = LeadToInvoiceSerializer(data=data)
# #         if serializer.is_valid():
# #             lead_to_invoice = serializer.save()  # Save the new LeadToInvoice instance
# #             return Response({"message": "Lead to Invoice record created!", "id": lead_to_invoice.id}, status=status.HTTP_201_CREATED)
# #         else:
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # class NumberingSystemSettingsAPI(APIView):
# #     queryset = NumberingSystemSettings.objects.all()
# #     def get(self, request):
# #         settings = NumberingSystemSettings.objects.all()
# #         serializer = NumberingSystemSettingsSerializer(settings, many=True)
# #         return Response(serializer.data)

# from rest_framework.views import APIView


# from rest_framework.response import Response
# from rest_framework import status
# from .models import (
#     Lead,
#     Quotation,
#     Invoice,
#     NumberingSystemSettings,
#     Notification,
#     LeadToInvoice,
# )
# from .serializers import (
#     LeadSerializer,
#     QuotationSerializer,
#     InvoiceSerializer,
#     NumberingSystemSettingsSerializer,
#     NotificationSerializer,
#     LeadToInvoiceSerializer,
# )


# # Function to generate unique numbers based on the numbering system settings
# def generate_number(type):
#     settings = NumberingSystemSettings.objects.get(type=type)
#     current_number = settings.current_number
#     new_number = f"{settings.prefix or ''}{current_number}{settings.suffix or ''}"
#     settings.current_number += settings.increment_step
#     settings.save()
#     return new_number


# class CreateLeadView(APIView):
#     queryset = Lead.objects.all()

#     def post(self, request):
#         data = request.data
#         data["lead_number"] = generate_number("Lead")
#         lead = Lead.objects.create(**data)
#         return Response(
#             {"message": "Lead created!", "lead_number": lead.lead_number},
#             status=status.HTTP_201_CREATED,
#         )

#     def get(self, request):
#         leads = Lead.objects.all()
#         serializer = LeadSerializer(leads, many=True)
#         return Response(serializer.data)


# class CreateQuotationView(APIView):
#     queryset = Quotation.objects.all()

#     def post(self, request):
#         data = request.data
#         try:
#             lead = Lead.objects.get(id=data["lead_id"])
#         except Lead.DoesNotExist:
#             return Response(
#                 {"error": "Lead not found"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         data["quotation_number"] = generate_number("Quotation")
#         quotation = Quotation.objects.create(lead=lead, **data)
#         return Response(
#             {
#                 "message": "Quotation created!",
#                 "quotation_number": quotation.quotation_number,
#             },
#             status=status.HTTP_201_CREATED,
#         )

#     def get(self, request):
#         quotations = Quotation.objects.all()
#         serializer = QuotationSerializer(quotations, many=True)
#         return Response(serializer.data)


# class CreateInvoiceView(APIView):
#     queryset = Invoice.objects.all()

#     def post(self, request):
#         data = request.data
#         try:
#             quotation = Quotation.objects.get(id=data["quotation_id"])
#         except Quotation.DoesNotExist:
#             return Response(
#                 {"error": "Quotation not found"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         data["invoice_number"] = generate_number("Invoice")
#         invoice = Invoice.objects.create(quotation=quotation, **data)
#         return Response(
#             {"message": "Invoice created!", "invoice_number": invoice.invoice_number},
#             status=status.HTTP_201_CREATED,
#         )

#     def get(self, request):
#         invoices = Invoice.objects.all()
#         serializer = InvoiceSerializer(invoices, many=True)
#         return Response(serializer.data)


# # class NotificationAPI(APIView):
# #     queryset = Notification.objects.all()

# #     def post(self, request):
# #         data = request.data
# #         notification = Notification.objects.create(**data)
# #         return Response({"message": "Notification created!", "notification_id": notification.id}, status=status.HTTP_201_CREATED)

# #     def get(self, request):
# #         notifications = Notification.objects.all()
# #         serializer = NotificationSerializer(notifications, many=True)
# #         return Response(serializer.data)


# class LeadToInvoiceView(APIView):
#     queryset = LeadToInvoice.objects.all()

#     def get(self, request):
#         leads = Lead.objects.all()
#         quotations = Quotation.objects.filter(lead__in=leads)
#         invoices = Invoice.objects.filter(quotation__in=quotations)

#         data = []
#         for invoice in invoices:
#             data.append(
#                 {
#                     "lead": invoice.quotation.lead.name,
#                     "quotation_number": invoice.quotation.quotation_number,
#                     "invoice_number": invoice.invoice_number,
#                     "amount_due": invoice.amount_due,
#                     "status": invoice.status,
#                 }
#             )

#         return Response(data)

#     def post(self, request):
#         data = request.data

#         serializer = LeadToInvoiceSerializer(data=data)
#         if serializer.is_valid():
#             lead_to_invoice = serializer.save()
#             return Response(
#                 {
#                     "message": "Lead to Invoice record created!",
#                     "id": lead_to_invoice.id,
#                 },
#                 status=status.HTTP_201_CREATED,
#             )
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class NumberingSystemSettingsAPI(APIView):
#     queryset = NumberingSystemSettings.objects.all()

#     def get(self, request):
#         settings = NumberingSystemSettings.objects.all()
#         serializer = NumberingSystemSettingsSerializer(settings, many=True)
#         return Response(serializer.data)


# class NotificationAPI(APIView):
#     queryset = Notification.objects.all()

#     def post(self, request):
#         data = request.data

#         # Handle 'lead' field
#         lead_id = data.get("lead")
#         if lead_id:
#             try:
#                 lead_instance = Lead.objects.get(id=lead_id)
#                 data["lead"] = lead_instance
#             except Lead.DoesNotExist:
#                 return Response(
#                     {"message": "Lead not found!"}, status=status.HTTP_404_NOT_FOUND
#                 )

#         quotation_id = data.get("quotation")
#         if quotation_id:
#             try:
#                 quotation_instance = Quotation.objects.get(id=quotation_id)
#                 data["quotation"] = quotation_instance
#             except Quotation.DoesNotExist:
#                 return Response(
#                     {"message": "Quotation not found!"},
#                     status=status.HTTP_404_NOT_FOUND,
#                 )

#         try:
#             notification = Notification.objects.create(**data)
#             return Response(
#                 {
#                     "message": "Notification created!",
#                     "notification_id": notification.id,
#                 },
#                 status=status.HTTP_201_CREATED,
#             )

#         except Exception as e:
#             return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request):
#         notifications = Notification.objects.all()
#         serializer = NotificationSerializer(notifications, many=True)
#         return Response(serializer.data)


# # has context menu


from rest_framework.views import APIView


from rest_framework.response import Response
from rest_framework import status
from .models import (
    Lead,
    Quotation,
    Invoice,
    NumberingSystemSettings,
    Notification,
    LeadToInvoice,
)
from .serializers import (
    LeadSerializer,
    QuotationSerializer,
    InvoiceSerializer,
    NumberingSystemSettingsSerializer,
    NotificationSerializer,
    LeadToInvoiceSerializer,
)


# Function to generate unique numbers based on the numbering system settings
def generate_number(type):
    settings = NumberingSystemSettings.objects.get(type=type)
    current_number = settings.current_number
    new_number = f"{settings.prefix or ''}{current_number}{settings.suffix or ''}"
    settings.current_number += settings.increment_step
    settings.save()
    return new_number


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


class CreateQuotationView(APIView):
    queryset = Quotation.objects.all()

    def post(self, request):
        data = request.data
        try:
            lead = Lead.objects.get(id=data["lead_id"])
        except Lead.DoesNotExist:
            return Response(
                {"error": "Lead not found"}, status=status.HTTP_400_BAD_REQUEST
            )

        data["quotation_number"] = generate_number("Quotation")
        quotation = Quotation.objects.create(lead=lead, **data)
        return Response(
            {
                "message": "Quotation created!",
                "quotation_number": quotation.quotation_number,
            },
            status=status.HTTP_201_CREATED,
        )

    def get(self, request):
        quotations = Quotation.objects.all()
        serializer = QuotationSerializer(quotations, many=True)
        return Response(serializer.data)


class CreateInvoiceView(APIView):
    queryset = Invoice.objects.all()

    def post(self, request):
        data = request.data
        try:
            quotation = Quotation.objects.get(id=data["quotation_id"])
        except Quotation.DoesNotExist:
            return Response(
                {"error": "Quotation not found"}, status=status.HTTP_400_BAD_REQUEST
            )

        data["invoice_number"] = generate_number("Invoice")
        invoice = Invoice.objects.create(quotation=quotation, **data)
        return Response(
            {"message": "Invoice created!", "invoice_number": invoice.invoice_number},
            status=status.HTTP_201_CREATED,
        )

    def get(self, request):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)


# class NotificationAPI(APIView):
#     queryset = Notification.objects.all()

#     def post(self, request):
#         data = request.data
#         notification = Notification.objects.create(**data)
#         return Response({"message": "Notification created!", "notification_id": notification.id}, status=status.HTTP_201_CREATED)

#     def get(self, request):
#         notifications = Notification.objects.all()
#         serializer = NotificationSerializer(notifications, many=True)
#         return Response(serializer.data)


class LeadToInvoiceView(APIView):
    queryset = LeadToInvoice.objects.all()

    def get(self, request):
        leads = Lead.objects.all()
        quotations = Quotation.objects.filter(lead__in=leads)
        invoices = Invoice.objects.filter(quotation__in=quotations)

        data = []
        for invoice in invoices:
            data.append(
                {
                    "lead": invoice.quotation.lead.name,
                    "quotation_number": invoice.quotation.quotation_number,
                    "invoice_number": invoice.invoice_number,
                    "amount_due": invoice.amount_due,
                    "status": invoice.status,
                }
            )

        return Response(data)

    def post(self, request):
        data = request.data

        serializer = LeadToInvoiceSerializer(data=data)
        if serializer.is_valid():
            lead_to_invoice = serializer.save()
            return Response(
                {
                    "message": "Lead to Invoice record created!",
                    "id": lead_to_invoice.id,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NumberingSystemSettingsAPI(APIView):
    queryset = NumberingSystemSettings.objects.all()

    def get(self, request):
        settings = NumberingSystemSettings.objects.all()
        serializer = NumberingSystemSettingsSerializer(settings, many=True)
        return Response(serializer.data)


class NotificationAPI(APIView):
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
