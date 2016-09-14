from flask import Flask, render_template, url_for, jsonify, redirect, request, flash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base

app = Flask(__name__)

engine = create_engine('postgresql://wilding:password@localhost/playground')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
