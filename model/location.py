from sqlalchemy import *
from sqlalchemy.orm import relationship

from config.base import Base


class Location(Base):
    __tablename__ = "target_location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    country_id = Column(Integer, ForeignKey("countries.id"))

    city = relationship("City", back_populates="location")
    country = relationship("Country", back_populates="location")
    target = relationship("Target", back_populates="location")
    def __repr__(self):
        return f"Location<(id={self.id}, city={self.city.name}, country={self.country.name})>"
