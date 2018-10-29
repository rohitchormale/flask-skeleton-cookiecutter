"""
This module implements various models related with User extension


@author: {{ cookiecutter.author }}
"""


from app import db


class BaseModel(db.model):
    """
    Abstract model
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp, onupdate=db.func.current_timestamp)



