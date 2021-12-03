from app import app
from flask import render_template
from models.shopping_list import *

@app.route('/list')
def shopping_list():
    return render_template('index.html', title= "Shopping List", items=items)