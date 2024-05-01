from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/products', methods=['GET'])
def products():
    return render_template('products.html')


@app.route('/contacts', methods=['GET'])
def contacts():
    return render_template('contacts.html')
