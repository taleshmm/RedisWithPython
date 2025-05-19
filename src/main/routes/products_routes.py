from flask import Blueprint, request, jsonify

products_routes_bp = Blueprint("products_routes", __name__)

@products_routes_bp.route("/products", methods=["POST"])
def insert_product():
    body = request.get_json()
    name = body.get("name")
    price = body.get("price")
    quantity = body.get("quantity")
    
    return jsonify({
        "type": "PRODUCT",
        "count": 1,
        "message": "Product created successfully"
    }), 201
    
@products_routes_bp.route("/products/<string:product_name>", methods=["GET"])
def get_product(product_name):
    return jsonify({"data": product_name
    }), 200