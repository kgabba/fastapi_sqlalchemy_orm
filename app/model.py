from sqlalchemy.orm import declarative_base, mapped_column, Mapped
from sqlalchemy import  BigInteger, String, ForeignKey

Base = declarative_base()

#тут конечно с mapped такая морока, что лучше в следующий раз использовать просто Column! 
class BaseModelOrm(Base):
    __abstract__=True
    id: Mapped['int'] = mapped_column(BigInteger, autoincrement=True, primary_key=True)

class User(BaseModelOrm):
    __tablename__ = 'users'
    username: Mapped['str'] = mapped_column(String)
    team_id: Mapped['int'] = mapped_column(BigInteger, ForeignKey('teams.id'))
    position: Mapped['str'] = mapped_column(String)
    score: Mapped['int'] = mapped_column(BigInteger)

class Team(BaseModelOrm):
    __tablename__ = 'teams'
    name: Mapped['str'] = mapped_column(String)
    district: Mapped['str'] = mapped_column(String)
