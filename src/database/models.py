import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

class CheckerLists(Base): 
    __tablename__ = 'checker_lists'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    checker_list_github = sa.Column(sa.ARRAY(sa.String))
    checker_list_twitch = sa.Column(sa.ARRAY(sa.String))
    checker_list_vk = sa.Column(sa.ARRAY(sa.String))
    checker_list_discord = sa.Column(sa.ARRAY(sa.String))
    checker_list_telegram = sa.Column(sa.ARRAY(sa.String))
    user_id = sa.Column(sa.BigInteger, nullable=False)

Base.metadata.create_all(engine)