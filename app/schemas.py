# app/schemas.py

'''
Marshmallow Schemas for each model
Asists in serialization and pretty printing of objects
'''

from app import ma
from marshmallow import fields
from .models import Url, Comment

# URL Marshmallow Schema
class UrlSchema(ma.Schema):
    comments = fields.Nested('CommentSchema', many=True, only=['id','comment'])
    class Meta:
        fields = ('id', 'uri', 'comments')

# Comment Marshmallow Schema
class CommentSchema(ma.Schema):
    url = fields.Nested('UrlSchema', only=['id', 'uri'])
    class Meta:
        fields = ('id', 'url', 'comment')

# Init Schemas
url_schema = UrlSchema()
urls_schema = UrlSchema(many=True)
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)