from sqlalchemy import Column, ForeignKey, Ingeger, String, Boolean, Date, DateTime, Enum, Float, Interval, PickleType, Time, Unicode, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


engine = create_engine('postgresql://wilding:password@localhost/playground')
Base.metadata.create_all(engine)
