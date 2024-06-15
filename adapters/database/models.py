from sqlalchemy import Column, String, Uuid
from .base import Base


class UserModel(Base):
    __tablename__ = "users"
    id = Column("id", Uuid, primary_key=True, nullable=False)
    username = Column("username", String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)
    email = Column("email", String, nullable=False)
