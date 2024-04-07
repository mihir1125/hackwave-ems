from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from model import get_sql
import datetime
import pandas as pd

import mysql.connector
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/hackwave'
app.config['SECRET_KEY'] = 'hackwaveems'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hackwave'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Helper Functions

class Managers(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# def serialize_datetime(obj): 
    # if isinstance(obj, datetime.datetime): 
        # return obj.strftime("%Y-%m-%d %H:%M:%S")
    
@login_manager.user_loader
def load_user(user_id):
    return Managers.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    return render_template('index.html')
    
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

def validate_user(uname, pwd):
    try:
        user = Managers.query.filter_by(username=uname).first()
        print(user)
        if user and user.password == pwd:
            login_user(user)
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        flash('Invalid username or password.', 'error')
    return render_template('login.html')

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    uname = data.get('uname')
    pwd = data.get('pwd')

    if uname and pwd:
        if validate_user(uname, pwd):
            flash('Login successful!', 'success')
            print("successs")
            return json.dumps({"body": {"msg": "success"}})
        else:
            flash('Invalid username or password.', 'error')
            return json.dumps({"body": {"msg": "error"}})
    else:
        flash('Username and password are required.', 'error')
        return json.dumps({"body": {"msg": "error"}})
        
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))

@app.route('/chat', methods=['POST'])
@login_required
def chat():
    data = request.get_json()
    user_input = data.get('user_input')
    # Here you can process the user_input, maybe pass it to a chatbot model
    # and get a response
    # For demonstration purposes, let's just echo back the input
    sql_res = get_sql(user_input)
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'hackwave',
    )
    cur = conn.cursor()
    
    if "update" in sql_res.lower() or "insert" in sql_res.lower() or "delete" in sql_res.lower():
        print("will run commit")
        sql_res += "BEGIN; "
        conn.commit()
        print(f"Query: {sql_res}")
        cur.execute(sql_res)
    else:
        print(f"Query: {sql_res}")
        cur.execute(sql_res)
    
    bot_response = cur.fetchall()
    cur.close()
    conn.close()
    if len(bot_response) == 0:
        bot_response = "Done."
    else:
        df = pd.DataFrame(bot_response)
        bot_response = df.to_html()
    return json.dumps({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)