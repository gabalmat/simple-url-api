# app/schemas.py

'''
Marshmallow Schemas for each model
Asists in serialization and pretty printing objects
'''

from app import ma
from .models import Url, Comment

# URL Marshmallow Schema
class UrlSchema(ma.ModelSchema):
    class Meta:
        model = Url

# Comment Marshmallow Schema
class CommentSchema(ma.ModelSchema):
    class Meta:
        model = Comment

# Init Schemas
url_schema = UrlSchema(only=['id', 'uri'])
urls_schema = UrlSchema(many=True, only=['id', 'uri'])
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)