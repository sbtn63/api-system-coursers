from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated, PermissionDenied
from django.http import Http404

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    path = context['request'].path

    data = {
        "message": "Internal Server Error",
        "data": None,
        "status": 500,
        "path": path
    }

    if isinstance(exc, (AuthenticationFailed, NotAuthenticated)):
        data["message"] = "Invalid or missing token"
        data["status"] = 401

    elif isinstance(exc, PermissionDenied):
        data["message"] = "You do not have permissions for this"
        data["status"] = 403

    elif isinstance(exc, Http404) or (response and response.status_code == 404):
        data["message"] = str(exc)
        data["status"] = 404
        
    elif data["status"] == 500:
        data["data"] = str(exc)

    return Response(data, status=data["status"])