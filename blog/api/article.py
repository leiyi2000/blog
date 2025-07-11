import random

from django.http import HttpRequest, JsonResponse


async def read(request: HttpRequest, article_id: int):
    """模拟用户访问文章详情页

    Args:
        request (HttpRequest): request
        article_id (int): 文章ID
    """
    mock = {
        "article_id": article_id,
        "user_id": random.randint(10000, 10030),
        "created_at": "2021-01-01 00:00:00",
    }
    return JsonResponse(mock)
