from combojsonapi.event.resource import EventsResource
from flask_rest_jsonapi import ResourceList, ResourceDetail

from blog.models import Author, Article
from blog.models.database import db
from blog.schemas import AuthorSchema


class AuthorDetailEvents(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return {"count": Article.query.filter_by(Article.author_id == kwargs["id"]).count()}

class AuthorList(ResourceList):
    events = AuthorDetailEvents
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        "session":db.session,
        "model": Author,
    }