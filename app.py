from flask import Flask, redirect, render_template, request, flash
from models import db, connect_db, Item, Warehouse
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'shh')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///inventory_app').replace("://", "ql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def homepage():
    return render_template('create-item.html')

@app.route('/items')
def list_items():
    items = Item.query.all()
    return render_template('items.html', items=items)

@app.route('/items', methods = ['POST'])
def create_item():
    id = request.form['id']
    name = request.form['name']
    description = request.form['description']

    try:
        new_item = Item(id = id, name = name, description = description)
        db.session.add(new_item)
        db.session.commit()
    except:
        flash("item id is required or duplicate id entered")
        return render_template("create-item.html")

    return redirect('/items')

@app.route('/item/<int:item_id>')
def item_details(item_id):
    item = Item.query.get_or_404(item_id)

    return render_template('item-details.html', item=item)

@app.route('/item/<int:item_id>', methods = ['POST'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)

    db.session.delete(item)
    db.session.commit()

    return redirect('/items')

@app.route('/item/<int:item_id>/edit')
def item_edit_form(item_id):
    item = Item.query.get_or_404(item_id)
    return render_template('edit-item.html', item=item)

@app.route('/item/<int:item_id>/edit', methods=['POST'])
def item_update(item_id):
   
    item = Item.query.get_or_404(item_id)

    try:
        item.id = request.form['id']
        item.name = request.form['name']
        item.description = request.form['description']
    
        db.session.add(item)
        db.session.commit()
    except:
        flash('duplicate id or no id entered')
        return redirect(f'/item/{item_id}/edit')

    return redirect('/items')

@app.route('/item/<int:item_id>/assign')
def assign_form(item_id):
    item = Item.query.get_or_404(item_id)
    warehouses = Warehouse.query.all()
    return render_template('assign-item.html', item=item, warehouses=warehouses)

@app.route('/item/<int:item_id>/assign', methods = ['POST'])
def assign_item(item_id):
    item = Item.query.get_or_404(item_id)
    try:
        item.warehosue = request.form['warehouse']
       
        db.session.add(item)
        db.session.commit()
    except:
        flash('no warehouse exists')
        return redirect(f'/item/{item_id}/assign')

@app.route('/create-warehouse')
def warehouse_form():
    return render_template('create-warehouse.html')

@app.route('/warehouse', methods=['POST'])
def create_warehouse():
   
    warehouse = request.form['warehouse']

    try:
        new_warehouse = Warehouse(name=warehouse)

        db.session.add(new_warehouse)
        db.session.commit()
    except:
        flash('warehouse already exists')
        return render_template('create-warehouse.html')

    return redirect('/items')
