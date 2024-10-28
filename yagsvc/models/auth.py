from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)

from yagsvc.models.account import UserDAO
from yagsvc.sqldb import sqldb


class FlaskDanceOauth(OAuthConsumerMixin, sqldb.Model):
    __tablename__ = "flask_dance_oauth"
    __table_args__ = {"schema": "accounts"}
    provider_user_id = Column(String(256), unique=True)
    user_id = Column(Integer, ForeignKey(UserDAO.id))
    user = sqldb.relationship(UserDAO)
