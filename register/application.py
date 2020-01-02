from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

db = SQL('sqlite:///register.db')

@app.route('/')
def index():
    rows = db.execute('select * from registrants')
    return render_template('index.html', rows=rows)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        db.execute('insert into registrants (name, email) values (:name, :email)', name=name, email=email)
        return redirect('/')