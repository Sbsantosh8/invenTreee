from django.db import models


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


# class Quotation(models.Model):
#     quotation_number = models.CharField(
#         max_length=50, unique=True, null=True, blank=True
#     )
#     lead = models.ForeignKey("Lead", on_delete=models.CASCADE)
#     original_quotation = models.ForeignKey(
#         "self",
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name="revisions",
#     )
#     revision_count = models.PositiveIntegerField(
#         default=0
#     )  # Tracks the revision number

#     items = models.JSONField(
#         default=list
#     )  # List of items in the quotation (product IDs, names, quantities, prices)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     discount = models.DecimalField(
#         max_digits=5, decimal_places=2, null=True, blank=True
#     )
#     tax = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
#     status = models.CharField(
#         max_length=50,
#         choices=[
#             ("draft", "Draft"),
#             ("sent", "Sent"),
#             ("accepted", "Accepted"),
#             ("rejected", "Rejected"),
#         ],
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = "Quotation"
#         verbose_name_plural = "Quotations"
#         ordering = ["-created_at"]
#         unique_together = ["quotation_number"]
#         indexes = [
#             models.Index(fields=["lead", "status"]),
#         ]

#     def save(self, *args, **kwargs):
#         if not self.quotation_number:
#             if self.original_quotation:
#                 # Find the highest revision number for the same original quotation
#                 revisions = Quotation.objects.filter(
#                     original_quotation=self.original_quotation
#                 )
#                 if revisions.exists():
#                     # Extract the highest revision number
#                     max_revision = max(
#                         [
#                             int(revision.quotation_number.split(".")[-1])
#                             for revision in revisions
#                             if "." in revision.quotation_number
#                         ],
#                         default=0,
#                     )
#                     # Increment the revision number

#                     self.quotation_number = (
#                         f"{self.original_quotation.quotation_number}.{max_revision + 1}"
#                     )
#                 else:
#                     # If no revisions, this is the first revision, append .1
#                     self.quotation_number = (
#                         f"{self.original_quotation.quotation_number}.1"
#                     )
#             else:
#                 # For the original quotation, use the normal generation
#                 self.quotation_number = self.generate_quotation_number()

#         super().save(*args, **kwargs)

#     # def save(self, *args, **kwargs):
#     #     if not self.quotation_number:
#     #         if self.original_quotation:
#     #             # Generate a revised quotation number
#     #             self.revision_count = self.original_quotation.revisions.count() + 1
#     #             self.quotation_number = (
#     #                 f"{self.original_quotation.quotation_number}.{self.revision_count}"
#     #             )
#     #         else:
#     #             # Generate a new quotation number for the original
#     #             self.quotation_number = self.generate_quotation_number()
#     #     super().save(*args, **kwargs)

#     def generate_quotation_number(self):
#         """
#         Generate a unique quotation number for new quotations.
#         The format will be QN-MONTH-YEAR.
#         """
#         current_month = self.created_at.month
#         current_year = self.created_at.year
#         # Get the latest revision count for the same month and year
#         revision_count = (
#             Quotation.objects.filter(
#                 created_at__month=current_month, created_at__year=current_year
#             ).count()
#             + 1
#         )
#         return f"QN-{current_month:02d}-{current_year}-{revision_count}"

#     # def generate_quotation_number(self):
#     #     """
#     #     Generate a unique quotation number for new quotations.
#     #     This can be customized based on your system's requirements.
#     #     """
#     #     return f"{self.lead.id}-{int(self.created_at.timestamp())}"

#     # def get_revisions(self):
#     #     """
#     #     Get all revisions for this quotation.
#     #     """
#     #     return self.revisions.all()


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

    def save(self, *args, **kwargs):
        print(
            "Starting the save method..................."
        )  # Debugging start of the save method
        print("self quotation...............", self.quotation_number)
        if not self.quotation_number:
            print(
                "No quotation number found. Proceeding to generate one.................."
            )  # Debugging when quotation number is missing

            if self.original_quotation:
                print(
                    f"Original Quotation found:.................... {self.original_quotation.quotation_number}"
                )  # Debugging original quotation

                # Find the highest revision number for the same original quotation
                revisions = Quotation.objects.filter(
                    original_quotation=self.original_quotation
                )
                print(
                    f"Found {len(revisions)} revisions for this original quotation......................"
                )  # Debugging number of revisions

                if revisions.exists():
                    # Extract the highest revision number
                    max_revision = max(
                        [
                            int(revision.quotation_number.split(".")[-1])
                            for revision in revisions
                            if "." in revision.quotation_number
                        ],
                        default=0,
                    )
                    print(
                        f"Max revision found:....................... {max_revision}"
                    )  # Debugging the highest revision number

                    # Increment the revision number
                    self.quotation_number = (
                        f"{self.original_quotation.quotation_number}.{max_revision + 1}"
                    )
                    print(
                        f"New quotation number (revised):....................... {self.quotation_number}"
                    )  # Debugging the new quotation number
                else:
                    # If no revisions, this is the first revision, append .1
                    self.quotation_number = (
                        f"{self.original_quotation.quotation_number}.1"
                    )
                    print(
                        f"New quotation number (first revision):........................ {self.quotation_number}"
                    )  # Debugging first revision number
            else:
                print(
                    "No original quotation found. Generating a new quotation number..........................."
                )  # Debugging when no original quotation
                # For the original quotation, use the normal generation
                self.quotation_number = self.generate_quotation_number()
                print(
                    f"New quotation number (original):....................... {self.quotation_number}"
                )  # Debugging new quotation number for original
        else:
            print(
                f"Quotation number already exists:...................................... {self.quotation_number}"
            )  # Debugging when quotation number already exists

        super().save(*args, **kwargs)
        print(
            "Quotation saved successfully............................"
        )  # Debugging after save

    def generate_quotation_number(self):
        """
        Generate a unique quotation number for new quotations.
        The format will be QN-MONTH-YEAR.
        """
        current_month = self.created_at.month
        current_year = self.created_at.year
        # Get the latest revision count for the same month and year
        revision_count = (
            Quotation.objects.filter(
                created_at__month=current_month, created_at__year=current_year
            ).count()
            + 1
        )
        print(
            f"..................generate_quotation_number...................................QN-{current_month:02d}-{current_year}-{revision_count}"
        )
        return f"QN-{current_month:02d}-{current_year}-{revision_count}"

    # def generate_quotation_number(self):
    #     """
    #     Generate a unique quotation number for new quotations.
    #     This can be customized based on your system's requirements.
    #     """
    #     return f"{self.lead.id}-{int(self.created_at.timestamp())}"

    # def get_revisions(self):
    #     """
    #     Get all revisions for this quotation.
    #     """
    #     return self.revisions.all()


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, default=1)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_date = models.DateTimeField()
    status = models.CharField(
        max_length=50,
        choices=[
            ("unpaid", "Unpaid"),
            ("paid", "Paid"),
            ("partially_paid", "Partially Paid"),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice for {self.quotation.lead.name}"

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
        ordering = ["-created_at"]
        unique_together = ["invoice_number"]
        indexes = [
            models.Index(fields=["lead", "status"]),
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
