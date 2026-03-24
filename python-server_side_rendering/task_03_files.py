from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_products():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv_products():
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)


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
    else:
        return render_template('product_display.html', error='Wrong source')

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
