from sqlalchemy import *
from sqlalchemy.orm import relationship

from config.base import Base


class Target(Base):
    __tablename__ = "targets"
    id = Column(Integer, primary_key=True, autoincrement=True)
    coordinates_id = Column(Integer, ForeignKey("coordinates.id"))
    location_id = Column(Integer, ForeignKey("location.id"))
    type_id = Column(Integer, ForeignKey("types.id"))
    industry_id = Column(Integer, ForeignKey("industries.id"))
    priority = Column(Integer)

    coordinate = relationship("Coordinate", back_populates="target")
    location = relationship("Location", back_populates="target")
    type = relationship("Type", back_populates="target")
    industry = relationship("Industry", back_populates="target")

    def __repr__(self):
        return f"Target<(id={self.id}, lat={self.coordinate.lat}, lon={self.coodingate.lon}, city={self.location.city}, country={self.loaction.country}, type={self.type.type}, industry={self.industry.industry}, priority={self.priority})>"
