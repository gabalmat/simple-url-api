# app/models.py

from app import db, ma
from sqlalchemy.orm import relationship

# URL Class/Model
class Url(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    uri = db.Column(db.Text)
    comments = relationship('Comment', backref='url')

    def __init__(self, uri):
        self.uri = uri

# Comment Class/Model
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('urls.id'))

    comment = db.Column(db.Text)

    def __init__(self, url_id, comment):
        self.url_id = url_id
        self.comment = comment