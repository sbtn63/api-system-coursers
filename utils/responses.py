from rest_framework.response import Response

def api_response(request, data, msg, status=200):
    return Response({
        "message": msg,
        "status": status,
        "data": data,
        "path": request.path
    }, status=status)