from ..models import ArticleAccess

from django.http import HttpRequest, JsonResponse


async def reads(request: HttpRequest):
    data = []
    async for access in ArticleAccess.all():
        data.append(
            {
                "id": access.id,
                "article_id": access.article_id,
                "user_id": access.user_id,
                "created_at": access.created_at,
            }
        )
    return JsonResponse(data, safe=False)
