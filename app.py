import sqlite3
import os.path
from flask import Flask, render_template, url_for, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length
from flask_bootstrap import Bootstrap

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "tpch.sqlite")

app = Flask(__name__)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tpch.sqlite'
app.config['SECRET_KEY'] = 'secretkey'

#------------------------------ class ____(FlaskForm) ------------------------------#
class InsertTuple(FlaskForm):
    a_agentkey = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "a_agentkey"})
    a_name = StringField(validators=[InputRequired(), Length(min=1, max=20)], render_kw={"placeholder": "a_name"})
    a_rolekey = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "a_rolekey"})
    a_originkey = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "a_originkey"})
    a_gender = StringField(validators=[InputRequired(), Length(min=1, max=10)], render_kw={"placeholder": "a_gender"})
    a_race = StringField(validators=[InputRequired(), Length(min=1, max=10)], render_kw={"placeholder": "a_race"})
    submit = SubmitField('Submit')


#-------------------------------- @app.route(____) --------------------------------#
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/roles', methods=['GET', 'POST'])
def roles():
    return render_template('roles.html')

@app.route('/IUD', methods=['GET', 'POST'])
def IUD():
    return render_template('IUD.html')

# Adding a new agent would also need to add info to KDA stats for each map (NEW = 0 stats for now)
@app.route('/insert', methods=['GET', 'POST'])
def inserttuple():
    form = InsertTuple()

    count = 1

    if form.validate_on_submit():
        a_agentkey = form.a_agentkey.data
        a_name = form.a_name.data
        a_rolekey = form.a_rolekey.data
        a_originkey = form.a_originkey.data
        a_gender = form.a_gender.data
        a_race = form.a_race.data

        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()

            insagent =  """INSERT INTO agents(a_agentkey,a_name,a_rolekey,a_originkey,a_gender,a_race) 
                VALUES ({},{},{},{},{}.{})""".format(a_agentkey, a_name, a_rolekey, a_originkey, a_gender, a_race)
            cur.execute(insagent)

            if count != 6:
                inskda = """INSERT INTO kda(kda_agentkey,kda_mapkey,kda_kill,kda_death,kda_assist,kda_winrate,kda_atkwin,kda_defwin,kda_agentpr) 
                    VALUES ({},{},0,0,0,0,0,0,0)""".format(a_agentkey, count)
                cur.execute(inskda)

                count += 1

    return render_template('insert.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
