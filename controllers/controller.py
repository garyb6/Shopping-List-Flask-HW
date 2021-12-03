from app import app
from flask import render_template, request
from models.shopping_list import *

@app.route('/list')
def shopping_list():
    return render_template('index.html', title= "Shopping List", items=items)

@app.route('/list', methods=['POST'])
def add_item():
    item_name = request.form['name']
    item_price = request.form['price']
    item_quantity = request.form['quantity']
    new_item = Items(item_name, item_price, item_quantity, False)
    add_new_item(new_item)
    return render_template ('index.html', title= "Shopping List", items=items)