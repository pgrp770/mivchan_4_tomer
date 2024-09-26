from sqlalchemy import *

from config.base import Base


class Type(Base):
    __tablename__ = "target_types"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(100), nullable=True)

    def __repr__(self):
        return f"City<(id={self.id}, name={self.id})>"