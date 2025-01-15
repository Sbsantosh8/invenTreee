# # # # inventree_audit_log/middleware.py
# # # import time
# # # import json
# # # from django.conf import settings
# # # from django.utils import timezone

# # # class AuditLogMiddleware:
# # #     def __init__(self, get_response):
# # #         self.get_response = get_response

# # #     def __call__(self, request):
# # #         if not getattr(settings, 'AUDIT_LOG_ENABLED', True):
# # #             return self.get_response(request)

# # #         start_time = time.time()

# # #         try:
# # #             # Process request
# # #             response = self.get_response(request)

# # #             # Create log entry
# # #             from .models import AuditLog
            
# # #             # Extract request payload safely
# # #             if request.content_type == 'application/json':
# # #                 try:
# # #                     payload = json.loads(request.body)
# # #                 except json.JSONDecodeError:
# # #                     payload = {}
# # #             else:
# # #                 payload = request.POST.dict()

# # #             # Create log entry
# # #             log_entry = AuditLog(
# # #                 request_method=request.method,
# # #                 request_url=request.get_full_path(),
# # #                 request_headers=json.dumps(dict(request.headers)),
# # #                 request_payload=json.dumps(payload),
# # #                 response_status=response.status_code,
# # #                 response_payload=str(response.content)[:1000],  # Limit response size
# # #                 user_id=request.user.id if request.user.is_authenticated else None,
# # #                 ip_address=request.META.get('REMOTE_ADDR'),
# # #                 duration_ms=int((time.time() - start_time) * 1000)
# # #             )

# # #             # Try to extract entity info from URL
# # #             try:
# # #                 parts = request.path.strip('/').split('/')
# # #                 if len(parts) >= 2:
# # #                     log_entry.entity = parts[0]
# # #                     if parts[1].isdigit():
# # #                         log_entry.entity_id = int(parts[1])
# # #             except:
# # #                 pass

# # #             log_entry.save()

# # #             return response

# # #         except Exception as e:
# # #             # Log error but don't break the request
# # #             print(f"Audit Log Error: {str(e)}")
# # #             return self.get_response(request)


# # import time
# # import json
# # from django.conf import settings
# # from django.utils import timezone

# # class AuditLogMiddleware:
# #     def __init__(self, get_response):
# #         self.get_response = get_response

# #     def __call__(self, request):
# #         if not getattr(settings, 'AUDIT_LOG_ENABLED', True):
# #             return self.get_response(request)

# #         start_time = time.time()

# #         try:
# #             # Process request
# #             response = self.get_response(request)

# #             # Create log entry
# #             from .models import AuditLog

# #             # Extract request payload safely
# #             if request.content_type == 'application/json' and not request.body_consumed:
# #                 try:
# #                     # Save the original body for logging without consuming it
# #                     request._body = request.body
# #                     request.body_consumed = True
# #                     payload = json.loads(request.body)
# #                 except json.JSONDecodeError:
# #                     payload = {}
# #             else:
# #                 payload = request.POST.dict()

# #             # Create log entry
# #             log_entry = AuditLog(
# #                 request_method=request.method,
# #                 request_url=request.get_full_path(),
# #                 request_headers=json.dumps(dict(request.headers)),
# #                 request_payload=json.dumps(payload),
# #                 response_status=response.status_code,
# #                 response_payload=str(response.content)[:1000],  # Limit response size
# #                 user_id=request.user.id if request.user.is_authenticated else None,
# #                 ip_address=request.META.get('REMOTE_ADDR'),
# #                 duration_ms=int((time.time() - start_time) * 1000)
# #             )

# #             # Try to extract entity info from URL
# #             try:
# #                 parts = request.path.strip('/').split('/')
# #                 if len(parts) >= 2:
# #                     log_entry.entity = parts[0]
# #                     if parts[1].isdigit():
# #                         log_entry.entity_id = int(parts[1])
# #             except:
# #                 pass

# #             log_entry.save()

# #             return response

# #         except Exception as e:
# #             # Log error but don't break the request
# #             print(f"Audit Log Error: {str(e)}")
# #             return self.get_response(request)


# import time
# import json
# from django.conf import settings
# from django.utils import timezone
# import io

# class AuditLogMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if not getattr(settings, 'AUDIT_LOG_ENABLED', True):
#             return self.get_response(request)

#         start_time = time.time()

#         try:
#             # Create a copy of the body so that it's accessible in the middleware without consuming it prematurely
#             request._body = request.body
#             request.body = io.BytesIO(request.body)  # Reset the body stream

#             # Process request
#             response = self.get_response(request)

#             # Create log entry
#             from .models import AuditLog

#             # Extract request payload safely
#             payload = {}
#             if request.content_type == 'application/json':
#                 try:
#                     # Read from the body and parse it
#                     request.body.seek(0)  # Ensure we're at the start of the body stream
#                     payload = json.loads(request.body.read().decode('utf-8'))
#                 except json.JSONDecodeError:
#                     payload = {}
#             else:
#                 payload = request.POST.dict()

#             # Create log entry
#             log_entry = AuditLog(
#                 request_method=request.method,
#                 request_url=request.get_full_path(),
#                 request_headers=json.dumps(dict(request.headers)),
#                 request_payload=json.dumps(payload),
#                 response_status=response.status_code,
#                 response_payload=str(response.content)[:1000],  # Limit response size
#                 user_id=request.user.id if request.user.is_authenticated else None,
#                 ip_address=request.META.get('REMOTE_ADDR'),
#                 duration_ms=int((time.time() - start_time) * 1000)
#             )

#             # Try to extract entity info from URL
#             try:
#                 parts = request.path.strip('/').split('/')
#                 if len(parts) >= 2:
#                     log_entry.entity = parts[0]
#                     if parts[1].isdigit():
#                         log_entry.entity_id = int(parts[1])
#             except:
#                 pass

#             log_entry.save()

#             return response

#         except Exception as e:
#             # Log error but don't break the request
#             print(f"Audit Log Error: {str(e)}")
#             return self.get_response(request)




import time
import json
from django.conf import settings
from django.utils import timezone
import io

class AuditLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not getattr(settings, 'AUDIT_LOG_ENABLED', True):
            return self.get_response(request)

        start_time = time.time()

        try:
            # Save the request body content for later without modifying the original 'body' attribute
            if not hasattr(request, '_body'):
                request._body = request.body  # Store the body in a custom attribute if not already done

            # Process request
            response = self.get_response(request)

            # Create log entry
            from .models import AuditLog

            # Extract request payload safely
            payload = {}
            if request.content_type == 'application/json':
                try:
                    # Read from the stored body content
                    payload = json.loads(request._body.decode('utf-8'))
                except json.JSONDecodeError:
                    payload = {}
            else:
                payload = request.POST.dict()

            # Create log entry
            log_entry = AuditLog(
                request_method=request.method,
                request_url=request.get_full_path(),
                request_headers=json.dumps(dict(request.headers)),
                request_payload=json.dumps(payload),
                response_status=response.status_code,
                response_payload=str(response.content)[:1000],  # Limit response size
                user_id=request.user.id if request.user.is_authenticated else None,
                ip_address=request.META.get('REMOTE_ADDR'),
                duration_ms=int((time.time() - start_time) * 1000)
            )

            # Try to extract entity info from URL
            try:
                parts = request.path.strip('/').split('/')
                if len(parts) >= 2:
                    log_entry.entity = parts[0]
                    if parts[1].isdigit():
                        log_entry.entity_id = int(parts[1])
            except:
                pass

            log_entry.save()

            return response

        except Exception as e:
            # Log error but don't break the request
            print(f"Audit Log Error: {str(e)}")
            return self.get_response(request)
