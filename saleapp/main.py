from saleapp import app, utils
from flask import render_template


@app.route("/")
def index():
    categories = utils.read_data()
    return render_template('index.html', categories=categories)


@app.route("/products")
def list_products():
    products = utils.read_data(path='data/products.json')
    return render_template('products.html', products=products)


@app.route("/products/<int:product_id>")
def product_detail(product_id):
   product = utils.get_product_by_id(product_id=product_id)

   return render_template('product-detail.html', product=product)


if __name__ == "__main__":
    app.run(debug=True)