from django.http import JsonResponse


async def ping(request):
    return JsonResponse({"status": "ok"})
