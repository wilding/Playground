import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Test

from flask import jsonify

# from datetime import datetime, timedelta

engine = create_engine('postgresql://vagrant:password@localhost/playground')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

tests = session.query(Test).all()
json_data = [test.serialize for test in tests]








test = open('test.json', 'w')

# test_dict = {
#     1: "Willie",
#     2: "Carla",
#     3: "Maryn",
#     4: "Ryan",
#     5: "Mombo",
#     6: ["Rosie", "Tom"]
# }

json.dump(json_data, test)
print 'done'

# test_dict1 = {
#     1: "Willie",
#     2: "Carla"
# }

# json.dump(test_dict1, test)










# with open('test.json') as json_data:
#     d = json.load(json_data)
#     print d['2']
