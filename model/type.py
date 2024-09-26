from sqlalchemy import *
from sqlalchemy.orm import relationship

from config.base import Base


class Type(Base):
    __tablename__ = "target_types"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(100), nullable=False)

    target = relationship("Target", back_populates="type")
    def __repr__(self):
        return f"Type<(id={self.id}, type={self.type})>"
