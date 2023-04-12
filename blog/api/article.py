from flask_rest_jsonapi import ResourceList, ResourceDetail

from blog.models import Article
from blog.models.database import db
from blog.schemas import ArticleSchema


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        "session":db.session,
        "model": Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session":db.session,
        "model": Article,
    }