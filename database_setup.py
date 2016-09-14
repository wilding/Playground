from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date, DateTime, Enum, Float, Interval, PickleType, Time, Unicode
# from sqlalchemy import Array, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


engine = create_engine('postgresql://vagrant:password@localhost/playground')
Base.metadata.create_all(engine)
