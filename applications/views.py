import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Application
from django.shortcuts import redirect

@csrf_exempt
def apply(request):
    # Only accept POST requests
    if request.method != "POST":
        return JsonResponse({"error": "Use POST"}, status=405)

    # Parse JSON body
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")

    # Validate required fields
    name = data.get("name")
    roll_number = data.get("roll_number")
    department = data.get("department")
    interests = data.get("interests", "")

    if not (name and roll_number and department):
        return JsonResponse(
            {"error": "Missing required fields: name, roll_number, department"},
            status=400,
        )

    # Save to DB
    app = Application.objects.create(
        name=name,
        roll_number=roll_number,
        department=department,
        interests=interests,
    )

    return JsonResponse({"message": "Application submitted", "application_id": app.id}, status=201)


def applications_list(request):
    # Only accept GET requests
    if request.method != "GET":
        return JsonResponse({"error": "Use GET"}, status=405)

    # Read all applications from DB, newest first
    apps = Application.objects.all().order_by("-applied_at")

    # Convert queryset to list of dicts
    data = [
        {
            "id": a.id,
            "name": a.name,
            "roll_number": a.roll_number,
            "department": a.department,
            "interests": a.interests,
            "applied_at": a.applied_at.isoformat(),
        }
        for a in apps
    ]

    return JsonResponse(data, safe=False)

