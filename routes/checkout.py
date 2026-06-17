from flask import Blueprint, request, jsonify

checkout_bp = Blueprint("checkout", __name__)

# In-memory storage
orders = []

@checkout_bp.route("/checkout", methods=["POST"])
def checkout():
    """VULNERABLE: Accepts price from client without validation"""
    data = request.get_json()
    
    # No validation on price field
    order = {
        "id": len(orders) + 1,
        "item": data.get("item", "Unknown"),
        "price": data.get("price", 0),
        "quantity": data.get("quantity", 1),
        "status": "pending"
    }
    
    orders.append(order)
    return jsonify(order), 201

@checkout_bp.route("/orders", methods=["GET"])
def list_orders():
    """Helper endpoint to view all orders"""
    return jsonify(orders)