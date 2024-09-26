from sqlalchemy import *

from config.base import Base


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=True)


    def __repr__(self):
        return f"City<(id={self.id}, name={self.id})>"