from .models import (
  
    NumberingSystemSettings,
  
)

# Function to generate unique numbers based on the numbering system settings

def generate_number(type):

    settings = NumberingSystemSettings.objects.get(type=type)
    current_number = settings.current_number
    print(" current_number....", current_number)
    new_number = f"{settings.prefix or ''}{current_number}{settings.suffix or ''}"
    settings.current_number += settings.increment_step
    settings.save()
    print("generate number working...........", new_number)
    return new_number

# from django.db import transaction

# def generate_number(type):
#     with transaction.atomic():
#         settings = NumberingSystemSettings.objects.select_for_update().get(type=type)
#         current_number = settings.current_number
#         print(" current_number....", current_number)
#         new_number = f"{settings.prefix or ''}{current_number}{settings.suffix or ''}"
#         settings.current_number += settings.increment_step
#         settings.save()
#         print("generate number working...........", new_number)
#         return new_number









