from sqlalchemy import Column, Integer, String, BigInteger

from app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True)
    username = Column(String(100), nullable=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    score = Column(Integer, default=0)
