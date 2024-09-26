from sqlalchemy import *

from config.base import Base


class Target(Base):
    __tablename__ = "targets"
    id = Column(Integer, primary_key=True, autoincrement=True)
    coordinates_id = Column(Integer, ForeignKey("coordinates.id"))
    location_id = Column(Integer, ForeignKey("location.id"))
    type_id = Column(Integer, ForeignKey("types.id"))
    industry_id = Column(Integer, ForeignKey("industries.id"))
    priority = Column(Integer)

    def __repr__(self):
        return f"City<(id={self.id}, name={self.id})>"
