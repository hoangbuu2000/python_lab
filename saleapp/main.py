from saleapp import app, utils
from flask import render_template, request


@app.route("/")
def index():
    categories = utils.read_data()
    return render_template('index.html', categories=categories)


@app.route("/products")
def list_products():
    products = utils.read_data(path='data/products.json')
    category = int(request.args.get('category_id')) if request.args.get('category_id') else None
    result = []
    if category:
        for p in products:
            if p["category_id"] == category:
                result.append(p)
    return render_template('products.html', products=result if category else products)


@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = utils.get_product_by_id(product_id=product_id)

    return render_template('product-detail.html', product=product)


if __name__ == "__main__":
    app.run(debug=True)