from flask import Flask, render_template, url_for, json, redirect, request, flash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Test

from datetime import datetime, timedelta

app = Flask(__name__)

engine = create_engine('postgresql://vagrant:password@localhost/playground')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def homepage():
    # session.rollback()
    tests = session.query(Test).all()
    return render_template('homepage.html', tests=tests)


@app.route('/test/new/', methods=['GET', 'POST'])
def newTest():
    if request.method == 'POST':
        form = parseForm(request.form)
        newtest = Test(
            integer=form['integer'],
            floatpt=form['floatpt'],
            string=request.form['string'],
            uni=request.form['uni'],
            boolean=form['boolean'],
            date=form['date'],
            time=form['time'],
            datetime=form['datetime'],
            interval=timedelta(days=form['days'], seconds=form['seconds'], microseconds=form['microseconds']),
            int_array=form['int_array'],
            str_array=form['str_array'],
            json_object=form['json_object']
            )
        session.add(newtest)
        session.commit()
        flash('New Test Added!')
        return redirect(url_for('homepage'))
    else:
        return render_template('newtest.html')


@app.route('/formplayground/')
def formPlayground():
    return render_template('formplayground.html')


# helper function
def parseForm(form):
    form_dict = {}
    form_dict['integer'] = form['integer'] if form['integer'] else 0
    form_dict['floatpt'] = form['floatpt'] if form['floatpt'] else 0.0
    form_dict['boolean'] = True if form.get('boolean') else False
    form_dict['date'] = datetime.strptime(form['date'], '%Y-%m-%d').date() if form['date'] else None
    form_dict['time'] = datetime.strptime(form['time'], '%H:%M').time() if form['time'] else None
    form_dict['datetime'] = datetime.strptime(form['datetime'], '%Y-%m-%dT%H:%M') if form['datetime'] else None
    form_dict['days'] = int(form['days']) if form['days'] else 0
    form_dict['seconds'] = int(form['seconds']) if form['seconds'] else 0
    form_dict['microseconds'] = int(form['microseconds']) if form['microseconds'] else 0
    int_array1 = int(form['int_array1']) if form['int_array1'] else 0
    int_array2 = int(form['int_array2']) if form['int_array2'] else 0
    int_array3 = int(form['int_array3']) if form['int_array3'] else 0
    form_dict['int_array'] = [int_array1, int_array2, int_array3]
    form_dict['str_array'] = [form['str_array1'], form['str_array2'], form['str_array3']]
    json_object = {
        "instructions": [
            {
                "text": 1,
                "image": 2,
                "video": 3,
                "gif": 4,
                "note": 5
            }
        ]
    }
    form_dict['json_object'] = json.dumps(json_object)
    return form_dict


if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
