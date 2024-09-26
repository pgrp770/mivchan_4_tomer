from sqlalchemy import *

from config.base import Base


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=True)

    def __repr__(self):
        return f"Country<(id={self.id}, name={self.id})>"