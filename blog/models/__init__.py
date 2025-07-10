from tortoise import Model, fields


class ArticleAccess(Model):
    id = fields.IntField(pk=True)
    article_id = fields.IntField()
    user_id = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
