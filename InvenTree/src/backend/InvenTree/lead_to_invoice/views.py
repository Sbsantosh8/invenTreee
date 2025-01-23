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
    print("generate number working...........", new_number)
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

    # def get(self, request):
    #     quotations = Quotation.objects.all()
    #     serializer = QuotationSerializer(quotations, many=True)
    #     return Response(serializer.data)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quotation, Lead  # Ensure your models are imported
from datetime import datetime


# Utility function to generate a unique quotation number
# def generate_number(prefix):
#     """
#     Generates a unique number for quotations based on the current timestamp.
#     Example: Quotation-20250121123456
#     """
#     now = datetime.now()
#     return f"{prefix}-{now.strftime('%Y%m%d%H%M%S')}"
def generate_quotation_number():
    """
    Generate a unique quotation number in the format QN-{incremental_id}-{year}.
    """
    current_year = datetime.now().year
    last_quotation = Quotation.objects.order_by("-id").first()

    # Determine the next incremental ID
    next_id = 1 if not last_quotation else last_quotation.id + 1

    # Construct the quotation number
    print(
        f"generate_quotation_number():         QN-{next_id}-{current_year}..................."
    )
    return f"QN-{next_id}-{current_year}"


# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt


# @method_decorator(csrf_exempt, name="dispatch")
# class CreateQuotationView(APIView):
#     queryset = Quotation.objects.all()

#     def get(self, request):
#         lead_id = request.query_params.get("lead_id")
#         status_filter = request.query_params.get("status")

#         # Filter quotations based on lead_id and/or status if provided
#         quotations = Quotation.objects.all()
#         if lead_id:
#             quotations = quotations.filter(lead_id=lead_id)
#         if status_filter:
#             quotations = quotations.filter(status=status_filter)

#         # Serialize the data
#         data = [
#             {
#                 "quotation_number": quotation.quotation_number,
#                 "lead_id": quotation.lead.id,
#                 "items": quotation.items,
#                 "total_amount": quotation.total_amount,
#                 "discount": quotation.discount,
#                 "tax": quotation.tax,
#                 "status": quotation.status,
#                 "created_at": quotation.created_at,
#                 "updated_at": quotation.updated_at,
#             }
#             for quotation in quotations
#         ]

#         return Response(data, status=status.HTTP_200_OK)

#     def post(self, request):
#         data = request.data
#         try:
#             # Validate if the provided lead exists
#             lead = Lead.objects.get(id=data["lead_id"])
#         except Lead.DoesNotExist:
#             return Response(
#                 {"error": "Lead not found"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         # Validate and extract items field
#         items = data.get("items")
#         if not isinstance(items, list) or not items:
#             return Response(
#                 {"error": "Items must be a non-empty list"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         # Generate a unique quotation number
#         data["quotation_number"] = generate_number("Quotation")

#         # Create the quotation object
#         quotation = Quotation.objects.create(
#             lead=lead,
#             quotation_number=data["quotation_number"],
#             items=items,
#             total_amount=data.get("total_amount", 0),
#             discount=data.get("discount", 0),
#             tax=data.get("tax", 0),
#             status=data.get("status", "draft"),
#         )

#         return Response(
#             {
#                 "message": "Quotation created!",
#                 "quotation_number": quotation.quotation_number,
#                 "items": quotation.items,
#                 "total_amount": quotation.total_amount,
#                 "discount": quotation.discount,
#                 "tax": quotation.tax,
#                 "status": quotation.status,
#             },
#             status=status.HTTP_201_CREATED,
#         )


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


from part.models import Part  # Assuming Part model exists and is related to items
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quotation


# @method_decorator(csrf_exempt, name="dispatch")
# class CreateQuotationView(APIView):
#     queryset = Quotation.objects.all()

#     def get(self, request):
#         lead_id = request.query_params.get("lead_id")
#         status_filter = request.query_params.get("status")

#         # Filter quotations based on lead_id and/or status if provided
#         quotations = Quotation.objects.all()
#         if lead_id:
#             quotations = quotations.filter(lead_id=lead_id)
#         if status_filter:
#             quotations = quotations.filter(status=status_filter)

#         # Serialize the data and ensure items are ordered and structured correctly
#         data = []
#         for quotation in quotations:
#             # Sort the items by any required field (optional)
#             items_sorted = sorted(
#                 quotation.items, key=lambda x: x.get("item_name", "")
#             )  # Sorting by item_name if required

#             # Ensure the items are in the correct order of keys
#             items_ordered = []
#             for item in items_sorted:
#                 ordered_item = {
#                     "item_name": item.get("item_name"),
#                     "quantity": item.get("quantity"),
#                     "price": item.get("price"),
#                     "total": item.get("total"),
#                 }
#                 items_ordered.append(ordered_item)

#             data.append(
#                 {
#                     "quotation_number": quotation.quotation_number,
#                     "lead_id": quotation.lead.id,
#                     "items": items_ordered,  # Use the ordered items
#                     "discount": quotation.discount,
#                     "tax": quotation.tax,
#                     "total_amount": quotation.total_amount,
#                     "status": quotation.status,
#                     "created_at": quotation.created_at,
#                     "updated_at": quotation.updated_at,
#                 }
#             )

#         return Response(data, status=status.HTTP_200_OK)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Lead, Quotation
from .serializers import QuotationSerializer
from part.models import Part
from django.db import transaction


class CreateQuotationView(APIView):
    def post(self, request):
        data = request.data
        parent_quotation_id = data.get("parent_quotation_id")
        print(
            "fetched parent_quotation_id........................", parent_quotation_id
        )

        try:
            lead = Lead.objects.get(id=data["lead_id"])
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

        # Generate quotation number
        with transaction.atomic():
            data["quotation_number"] = generate_number("Quotation")

            # Handle revision logic
            original_quotation = None
            if parent_quotation_id:
                try:
                    print("inside.... view ...............: ", parent_quotation_id)
                    parentObj = Quotation.objects.get(id=parent_quotation_id)
                    print(f"parentObj..........{parentObj}")
                    splitted_value = str(parentObj.quotation_number).split("-")
                    print(f"splitted_value..........{splitted_value}")
                    splitVal = float(splitted_value[-1]) + 0.1
                    print(f"splitVal..........{splitVal}")

                    print(
                        f"......{splitted_value[-3]}-{splitted_value[-2]}-{splitVal}........."
                    )

                    base_quotation_number = (
                        f"{splitted_value[-3]}-{splitted_value[-2]}-{splitVal:.1f}"
                    )
                    data["quotation_number"] = base_quotation_number
                    # original_quotation = Quotation.objects.get(id=parent_quotation_id)
                    # base_quotation_number = original_quotation.quotation_number.split(
                    #     "."
                    # )[0]

                    # # Find last revision
                    # last_revision = (
                    #     Quotation.objects.filter(original_quotation=original_quotation)
                    #     .order_by("-quotation_number")
                    #     .first()
                    # )

                    # if last_revision:
                    #     last_revision_number = float(
                    #         last_revision.quotation_number.split(".")[-1]
                    #     )
                    #     revision_no = last_revision_number + 0.1
                    # else:
                    #     revision_no = 0.1

                    # data["quotation_number"] = (
                    #     f"{base_quotation_number}.{revision_no:.1f}"
                    # )

                except Quotation.DoesNotExist:
                    return Response(
                        {"error": "Original quotation not found"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            # Create quotation
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


from django.shortcuts import get_object_or_404


class CreateRevisedQuotationAPI(APIView):
    def post(self, request, quotation_id):
        # Fetch the original quotation
        original_quotation = get_object_or_404(Quotation, id=quotation_id)

        # Generate a new quotation number for the revised quotation
        base_quotation_number = original_quotation.quotation_number
        revised_quotation_number = base_quotation_number

        # Check if the revised quotation number already exists
        revision_suffix = 1
        while Quotation.objects.filter(
            quotation_number=revised_quotation_number
        ).exists():
            revised_quotation_number = f"{base_quotation_number}.{revision_suffix}"
            revision_suffix += 1

        # Create the revised quotation
        revised_quotation = Quotation(
            lead=original_quotation.lead,
            total_amount=original_quotation.total_amount,
            discount=original_quotation.discount,
            tax=original_quotation.tax,
            status="draft",
            quotation_number=revised_quotation_number,  # Set the new unique quotation number
        )

        try:
            revised_quotation.save()
            return Response(
                {
                    "message": "Revised quotation created successfully.",
                    "revised_quotation_number": revised_quotation.quotation_number,
                },
                status=status.HTTP_201_CREATED,
            )  # HTTP 201 Created
        except Exception as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
