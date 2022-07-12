from .database import Base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship


class DbUser(Base):

    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)


class SensorConfig(Base):

    __tablename__ = "sensor_config"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    address = Column(String)
