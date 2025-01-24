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
from datetime import datetime
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










class CreateInvoiceView(APIView):
    queryset = Invoice.objects.all()
     
    def post(self, request):
        data = request.data
        try:
            quotation = Quotation.objects.get(id=data["quotation_id"])

            existing_invoice = Invoice.objects.filter(quotation=quotation).order_by('-created_at').first()
            print(f"existing invoice ....",existing_invoice)
            if existing_invoice:
                return Response(
                {"message": "An invoice already exists for this quotation", 
                 "invoice_details": InvoiceSerializer(existing_invoice).data}, 
                status=status.HTTP_400_BAD_REQUEST
            )
               


            
            # amount_due = quotation.total_amount - data["paid_amount"] 

            
        except Quotation.DoesNotExist:
            return Response(
                {"error": "Quotation not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        quotation = Quotation.objects.get(id=data["quotation_id"])
        
        try:
            lead = Lead.objects.get(id=data["lead_id"])

        except Lead.DoesNotExist:
            return Response(
                {"error": "Lead not found"}, status=status.HTTP_400_BAD_REQUEST
            )

   

        data["invoice_number"] = generate_number("Invoice")
        # print(f"quotation.total_amount : {quotation.total_amount}")
        # print(f"paid_amount: {data['paid_amount']}")
        # print(f"amount_due: {float(quotation.total_amount) - float(data['paid_amount'])}")
        
        # Assuming you have a 'total_amount' field in 'data'
        amount_due = float(quotation.total_amount) - float(data["paid_amount"])
        if amount_due == 0:
         return Response(
            {"message": "No invoice created. Amount due is zero."}, 
            status=status.HTTP_200_OK
        )
        data["amount_due"] = amount_due

        if amount_due == 0:
            return Response(
            {"message": "No invoice created. Amount due is zero."}, 
            status=status.HTTP_200_OK
        )


        invoice = Invoice.objects.create(quotation=quotation, **data)

        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # return Response(
        #     {"message": "Invoice created!", "invoice_number": invoice.invoice_number},
        #     status=status.HTTP_201_CREATED,
        # )

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
            for info in lead_to_invoice:
                print(info)
            return Response(
                {
                    "message": "Lead to Invoice record created!",
                    "id": lead_to_invoice.id,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class CreateQuotationView(APIView):
    def post(self, request):
        data = request.data
        parent_quotation_id = data.get("parent_quotation_id")
  

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
            ''' It goes to generate method,  saves data method, for without Decimal it will work  '''
            
            data["quotation_number"] = generate_number("Quotation")
                      
            ''' Main Quotation Revision Logic for incrementing'''

            # Handle revision logic
            original_quotation = None
            if parent_quotation_id:
                try:
                   
                    parentObj = Quotation.objects.get(id=parent_quotation_id)
                 
                    splitted_value = str(parentObj.quotation_number).split("-")
                 
                    splitVal = float(splitted_value[-1]) + 0.1
                  

                  
                    base_quotation_number = (
                        f"{splitted_value[-3]}-{splitted_value[-2]}-{splitVal:.1f}"
                    )
                    data["quotation_number"] = base_quotation_number
                  
                    
                    if  (data["quotation_number"][-1] == "0"):
                        data["quotation_number"] = data["quotation_number"][0:-2]

                except Quotation.DoesNotExist:
                    return Response(
                        {"error": "Parent quotation not found"},
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


