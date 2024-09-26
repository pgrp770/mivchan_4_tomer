from sqlalchemy import *
from sqlalchemy.orm import relationship

from config.base import Base


class Coordinate(Base):
    __tablename__ = "coordinates"
    id = Column(Integer, primary_key=True, autoincrement=True)
    lat = Column(Float, nullable=True)
    lon = Column(Float, nullable=True)

    target = relationship("Target", back_populates="coordinate")

    def __repr__(self):
        return f"City<(Coordinate={self.lat}, lon={self.lon})>"
