from flask_rest_jsonapi import ResourceList, ResourceDetail

from blog.models import Tag
from blog.models.database import db
from blog.schemas import TagSchema


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag
    }