from flask import Blueprint, request, jsonify

orders_bp = Blueprint("orders", __name__)

# Single order object for demonstration
order_data = {
    "id": 1,
    "email": "customer@test.com",
    "status": "pending",
    "isAdmin": False,
    "discount": 0
}

@orders_bp.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    """Get order details"""
    return jsonify(order_data)

@orders_bp.route("/orders/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    """VULNERABLE: Mass assignment - updates ALL fields provided"""
    data = request.get_json()
    
    # Directly updates all fields - NO FIELD FILTERING
    order_data.update(data)
    
    return jsonify(order_data)

@orders_bp.route("/orders/<int:order_id>/reset", methods=["POST"])
def reset_order(order_id):
    """Helper to reset order to original state"""
    global order_data
    order_data = {
        "id": 1,
        "email": "customer@test.com",
        "status": "pending",
        "isAdmin": False,
        "discount": 0
    }
    return jsonify({"message": "Reset successful", "order": order_data})