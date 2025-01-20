import time
import json
from django.conf import settings
from django.http import JsonResponse
from .models import AuditLog


class AuditLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not getattr(settings, "AUDIT_LOG_ENABLED", True):
            return self.get_response(request)

        start_time = time.time()
        log_entry = None
        payload = {}

        try:
            # Save the request body for later usage
            if not hasattr(request, "_body"):
                request._body = request.body  # Store the body in a custom attribute

            # Process request
            response = self.get_response(request)

            # Extract request payload safely
            if request.content_type == "application/json":
                try:
                    payload = json.loads(request._body.decode("utf-8"))
                except json.JSONDecodeError:
                    payload = {}
            else:
                payload = request.POST.dict()

            # Extract error message from the response if status is 4xx or 5xx
            error_message = None
            if 400 <= response.status_code < 600 and response.content:
                try:
                    response_data = json.loads(response.content.decode("utf-8"))
                    error_message = response_data.get("error")  # Extract "error" field
                except (json.JSONDecodeError, AttributeError):
                    error_message = response.content.decode("utf-8")[:1000]  # Fallback

            # Create log entry with response details
            log_entry = AuditLog(
                request_method=request.method,
                request_url=request.get_full_path(),
                request_headers=json.dumps(dict(request.headers)),
                request_payload=json.dumps(payload),
                response_status=response.status_code,
                response_payload=str(response.content)[:1000],  # Limit response size
                user_id=request.user.id if request.user.is_authenticated else None,
                ip_address=request.META.get("REMOTE_ADDR"),
                duration_ms=int((time.time() - start_time) * 1000),
                error_message=error_message,  # Save extracted error message here
            )

            # Extract entity info from URL
            parts = request.path.strip("/").split("/")
            if len(parts) >= 2:
                log_entry.entity = parts[0]
                if parts[1].isdigit():
                    log_entry.entity_id = int(parts[1])

            log_entry.save()

            return response

        except Exception as e:
            # Handle unexpected exceptions
            error_message = str(e)

            if log_entry is None:
                log_entry = AuditLog(
                    request_method=request.method,
                    request_url=request.get_full_path(),
                    request_headers=json.dumps(dict(request.headers)),
                    request_payload=json.dumps(payload) if payload else "{}",
                    response_status=500,
                    response_payload=f"Error: {str(e)}",
                    user_id=request.user.id if request.user.is_authenticated else None,
                    ip_address=request.META.get("REMOTE_ADDR"),
                    duration_ms=int((time.time() - start_time) * 1000),
                    error_message=error_message,  # Save the exception message here
                )
            else:
                log_entry.response_payload = f"Error: {str(e)}"
                log_entry.error_message = error_message

            log_entry.save()

            # Return a generic error response
            return JsonResponse(
                {"error": "An internal server error occurred."}, status=500
            )
