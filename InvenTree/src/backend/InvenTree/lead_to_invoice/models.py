from django.db import models
from django.forms import ValidationError
from django.db import transaction

class Lead(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("qualified", "Qualified"),
        ("converted", "Converted"),
        ("lost", "Lost"),
    ]
    lead_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    source = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="new")
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"
        ordering = ["-created_at"]
        unique_together = ["lead_number"]
        indexes = [
            models.Index(fields=["email"]),
        ]


class Quotation(models.Model):
    quotation_number = models.CharField(
        max_length=50, unique=True, null=True, blank=True
    )
    lead = models.ForeignKey("Lead", on_delete=models.CASCADE)
    original_quotation = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="revisions",
    )
    revision_count = models.PositiveIntegerField(
        default=0
    )  # Tracks the revision number

    items = models.JSONField(
        default=list
    )  # List of items in the quotation (product IDs, names, quantities, prices)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    tax = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ("draft", "Draft"),
            ("sent", "Sent"),
            ("accepted", "Accepted"),
            ("rejected", "Rejected"),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Quotation"
        verbose_name_plural = "Quotations"
        ordering = ["-created_at"]
        unique_together = ["quotation_number"]
        indexes = [
            models.Index(fields=["lead", "status"]),
        ]
    @transaction.atomic
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)     
            


    def get_revisions(self):
        """
        Get all revisions for this quotation.
        """
        return self.revisions.all()        

    def __str__(self):
        return self.quotation_number 
     

   
 
 
from django.db import models
from django.db.models import Sum
from decimal import Decimal
from django.core.exceptions import ValidationError


# class Invoice(models.Model):
#     invoice_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
#     amount_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     quotation = models.ForeignKey('Quotation', on_delete=models.CASCADE)
#     lead = models.ForeignKey('Lead', on_delete=models.CASCADE, default=1)  
#     paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     due_date = models.DateTimeField()
#     status = models.CharField(max_length=50, choices=[('unpaid', 'Unpaid'), ('paid', 'Paid'), ('partially_paid', 'Partially Paid')])
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     def save(self, *args, **kwargs):
#         if self.quotation:
#             self.total_amount = self.quotation.total_amount

#             # Ensure paid_amount is a Decimal
#             paid_amount_decimal = Decimal(self.paid_amount)

#             # Aggregate total paid for the quotation
#             total_paid = Invoice.objects.filter(quotation=self.quotation).aggregate(total_paid=Sum('paid_amount'))['total_paid'] or Decimal(0)

#             # Calculate remaining amount due
#             remaining_amount_due = self.total_amount - total_paid

#             # Validate if paid amount exceeds remaining amount due
#             try:
              
#                 if paid_amount_decimal > remaining_amount_due:
#                     raise ValueError(f"Already Paid amount Rs {total_paid}  ")
#             except ValueError as e:
#                 raise ValidationError(str(e))

#             # Ensure remaining amount due is not negative
#             if remaining_amount_due < 0:
#                 remaining_amount_due = Decimal(0)

#             # Calculate the amount_due for this invoice
#             self.amount_due = max(remaining_amount_due - paid_amount_decimal, Decimal(0))

#             # Set the status of the invoice based on amount_due
#             if self.amount_due == 0:
#                 self.status = 'paid'
#             elif self.amount_due < self.total_amount and self.amount_due > 0:
#                 self.status = 'partially_paid'
#             else:
#                 self.status = 'unpaid'

#         # Call the parent class save method
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"Invoice for {self.quotation.lead.name}"

#     class Meta:
#         verbose_name = "Invoice"
#         verbose_name_plural = "Invoices"
#         ordering = ['-created_at']
#         unique_together = ['invoice_number']
#         indexes = [
#             models.Index(fields=['lead', 'status']),
#         ]

from django.core.exceptions import ValidationError
from decimal import Decimal
from django.db.models import Sum
from django.db import transaction
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quotation = models.ForeignKey('Quotation', on_delete=models.CASCADE)
    lead = models.ForeignKey('Lead', on_delete=models.CASCADE, default=1)  
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('unpaid', 'Unpaid'), ('paid', 'Paid'), ('partially_paid', 'Partially Paid')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.quotation:
            self.total_amount = self.quotation.total_amount

            # Ensure paid_amount is a Decimal
            paid_amount_decimal = Decimal(self.paid_amount)

            # Aggregate total paid for the quotation
            total_paid = Invoice.objects.filter(quotation=self.quotation).aggregate(total_paid=Sum('paid_amount'))['total_paid'] or Decimal(0)

            # Calculate remaining amount due
            remaining_amount_due = self.total_amount - total_paid

            # Validate if paid amount exceeds remaining amount due
            if paid_amount_decimal > remaining_amount_due:
                raise ValidationError(f"You can only pay a maximum of Rs {remaining_amount_due}. You have already paid Rs {total_paid}.")

            # Ensure remaining amount due is not negative
            if remaining_amount_due < 0:
                remaining_amount_due = Decimal(0)

            # Calculate the amount_due for this invoice
            self.amount_due = max(remaining_amount_due - paid_amount_decimal, Decimal(0))

            # Set the status of the invoice based on amount_due
            if self.amount_due == 0:
                self.status = 'paid'
            elif self.amount_due < self.total_amount and self.amount_due > 0:
                self.status = 'partially_paid'
            else:
                self.status = 'unpaid'

        # Call the parent class save method
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice for {self.quotation.lead.name}"

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
        ordering = ['-created_at']
        unique_together = ['invoice_number']
        indexes = [
            models.Index(fields=['lead', 'status']),
        ]

class LeadToInvoice(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    quotation = models.ForeignKey(
        Quotation, on_delete=models.CASCADE, null=True, blank=True
    )
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, null=True, blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=[("created", "Created"), ("converted", "Converted")],
        default="created",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lead to Invoice: {self.lead.name} - {self.status}"

    class Meta:
        verbose_name = "Lead to Invoice"
        verbose_name_plural = "Leads to Invoices"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["lead", "status"]),
        ]


class NumberingSystemSettings(models.Model):
    TYPE_CHOICES = [
        ("Lead", "Lead"),
        ("Quotation", "Quotation"),
        ("Invoice", "Invoice"),
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES, unique=True)
    prefix = models.CharField(max_length=10, null=True, blank=True)
    suffix = models.CharField(max_length=10, null=True, blank=True)
    current_number = models.IntegerField(default=1)
    increment_step = models.IntegerField(default=1)
    reset_cycle = models.CharField(
        max_length=50,
        choices=[("monthly", "Monthly"), ("yearly", "Yearly")],
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.type} Numbering System"

    class Meta:
        verbose_name = "Numbering System Setting"
        verbose_name_plural = "Numbering System Settings"
        indexes = [
            models.Index(fields=["type"]),
        ]


class Notification(models.Model):
    NOTIFICATION_TYPE_CHOICES = [
        ("Email", "Email"),
        ("SMS", "SMS"),
        ("System", "System"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Sent", "Sent"),
        ("Failed", "Failed"),
    ]

    type = models.CharField(max_length=50, choices=NOTIFICATION_TYPE_CHOICES)
    recipient = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    timestamp = models.DateTimeField(auto_now_add=True)

    # New Relationships
    lead = models.ForeignKey(
        "Lead",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="notifications",
    )
    quotation = models.ForeignKey(
        "Quotation",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="notifications",
    )
    invoice = models.ForeignKey(
        "Invoice",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="notifications",
    )

    def __str__(self):
        return f"{self.type} Notification to {self.recipient}"

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ["-timestamp"]
        indexes = [
            models.Index(fields=["status"]),
        ]
