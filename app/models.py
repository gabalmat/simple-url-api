# app/models.py

from app import db

class Url(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    uri = db.Column(db.Text)

    def __repr__(self):
        return '<URL: {}'.format(self.uri)

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('urls.id'))
    comment = db.Column(db.Text)

    def __repr__(self):
        return '<URL ID: {}, Comment: {}>'.format(self.url_id, self.comment)