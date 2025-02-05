from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import generate_auth_token, verify_auth_token

@csrf_exempt
def generate_token_view(request):
    """
    API to generate an authentication token.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        org_id = data.get("org_id")
        org_name = data.get("org_name")

        if not username or not org_id or not org_name:
            return JsonResponse({"error": "Missing required parameters"}, status=400)

        token = generate_auth_token(username, org_id, org_name)
        return JsonResponse({"token": token})

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def verify_token_view(request):
    """
    API to verify an authentication token.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        org_id = data.get("org_id")
        org_name = data.get("org_name")
        token = data.get("token")

        if not username or not org_id or not org_name or not token:
            return JsonResponse({"error": "Missing required parameters"}, status=400)

        is_valid = verify_auth_token(username, org_id, org_name, token)
        return JsonResponse({"valid": is_valid})

    return JsonResponse({"error": "Invalid request method"}, status=405)
