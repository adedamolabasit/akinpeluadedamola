from personal import app,db
from flask import render_template



@app.route('/')
def index():
    return render_template('index.html')