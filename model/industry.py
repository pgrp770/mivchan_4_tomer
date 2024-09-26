from sqlalchemy import *
from sqlalchemy.orm import relationship

from config.base import Base


class Industry(Base):
    __tablename__ = "industries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    industry = Column(String(200), nullable=False)

    target = relationship("Target", back_populates="industry")
    def __repr__(self):
        return f"Industry<(id={self.id}, industry={self.industry})>"
