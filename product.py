from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy database
products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Phone", "price": 800}
]

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Get product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

# Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = {
        "id": len(products) + 1,
        "name": data.get("name"),
        "price": data.get("price")
    }
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

