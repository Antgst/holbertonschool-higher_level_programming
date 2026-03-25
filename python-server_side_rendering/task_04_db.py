from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_products():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv_products():
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)


def read_sql_products():
    conn = None
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except sqlite3.Error:
        return None
    finally:
        if conn:
            conn.close()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
    return render_template('items.html', items=data['items'])


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []

    if source == 'json':
        products = read_json_products()
    elif source == 'csv':
        products = read_csv_products()
    elif source == 'sql':
        products = read_sql_products()
    else:
        return render_template('product_display.html', error='Wrong source')

    if products is None:
        return render_template(
            'product_display.html',
            error='Error reading from database'
        )

    if product_id:
        products = [
            product for product in products
            if str(product.get('id')) == product_id
        ]

    if not products:
        return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
