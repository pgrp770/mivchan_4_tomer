from sqlalchemy import *

from config.base import Base


class Location(Base):
    __tablename__ = "target_location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    country_id = Column(Integer, ForeignKey("countries.id"))

    def __repr__(self):
        return f"City<(id={self.id}, name={self.id})>"