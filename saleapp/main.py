from saleapp import app, utils
from flask import render_template, request


@app.route("/")
def index():
    categories = utils.read_data()
    return render_template('index.html', categories=categories)


@app.route("/products")
def list_products():
    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')

    products = utils.read_product(cate_id=cate_id, kw=kw, from_price=from_price, to_price=to_price)

    return render_template('products.html', products=products, kw=kw, from_price=from_price, to_price=to_price)


@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = utils.get_product_by_id(product_id=product_id)

    return render_template('product-detail.html', product=product)


if __name__ == "__main__":
    app.run(debug=True)