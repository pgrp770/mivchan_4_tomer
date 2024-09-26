from sqlalchemy import *

from config.base import Base


class Coordinate(Base):
    __tablename__ = "target_location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    lat = Column(Float, nullable=True)
    lon = Column(Float, nullable=True)

    def __repr__(self):
        return f"City<(id={self.id}, name={self.id})>"