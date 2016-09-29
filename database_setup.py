from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date, DateTime, Float, Interval, Time, Unicode
# from sqlalchemy import Numeric, BigInteger, SmallInteger, Text, UnicodeText, Enum, PickleType, LargeBinary, MatchType, SchemaType
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# from enum import Enum


# class MyEnum(enum.Enum):
#     one = 'one'
#     two = 'two'
#     three = 'three'


Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    integer = Column(Integer)
    floatpt = Column(Float)
    string = Column(String(500))
    uni = Column(Unicode)
    boolean = Column(Boolean)
    date = Column(Date)
    time = Column(Time)
    datetime = Column(DateTime)
    interval = Column(Interval)
    int_array = Column(ARRAY(Integer))
    str_array = Column(ARRAY(String(9999)))
    json_object = Column(JSON)
    # enum = Column(Enum(MyEnum))


engine = create_engine('postgresql://vagrant:password@localhost/playground')
Base.metadata.create_all(engine)
