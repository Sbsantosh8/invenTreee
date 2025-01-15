# Generated by Django 4.2.16 on 2024-11-28 04:31

from django.db import migrations


def update_shipment_date(apps, schema_editor):
    """
    Update the shipment date for existing SalesOrderAllocation objects
    """

    from order.status_codes import SalesOrderStatusGroups

    SalesOrder = apps.get_model('order', 'SalesOrder')

    # Find any orders which are "complete" but missing a shipment date
    orders = SalesOrder.objects.filter(
        status__in=SalesOrderStatusGroups.COMPLETE,
        shipment_date__isnull=True
    )

    updated_orders = 0

    for order in orders:
        # Find the latest shipment date for any associated allocations
        shipments = order.shipments.filter(shipment_date__isnull=False)
        latest_shipment = shipments.order_by('-shipment_date').first()

        if not latest_shipment:
            continue

        # Update the order with the new shipment date
        order.shipment_date = latest_shipment.shipment_date
        order.save()

        updated_orders += 1
    
    if updated_orders > 0:
        print(f"Updated {updated_orders} SalesOrder objects with missing shipment_date")


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0104_alter_returnorderlineitem_quantity'),
    ]

    operations = [
        migrations.RunPython(
            update_shipment_date,
            reverse_code=migrations.RunPython.noop
        )
    ]
