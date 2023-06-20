import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, Query

from config import DATABASE_URL

engine = sa.create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String, nullable=False)
    user_id = sa.Column(sa.BIGINT, nullable=False)
    is_verification = sa.Column(sa.Boolean, nullable=False)
    password = sa.Column(sa.Integer, nullable=False)

Base.metadata.create_all(engine)