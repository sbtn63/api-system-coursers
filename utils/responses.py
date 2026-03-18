from rest_framework.response import Response

def api_response(request, data, msg, status=200):
    return Response({
        "message": msg,
        "data": data,
        "status": status,
        "path": request.path
    }, status=status)