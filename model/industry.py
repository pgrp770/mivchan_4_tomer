from sqlalchemy import *

from config.base import Base


class Industry(Base):
    __tablename__ = "industries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    industry = Column(String(100), nullable=True)

    def __repr__(self):
        return f"City<(id={self.id}, name={self.id})>"