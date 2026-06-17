from flask import Blueprint, request, jsonify
from datetime import datetime

webhook_bp = Blueprint("webhook", __name__)

processed_payments = []

@webhook_bp.route("/webhook/payment", methods=["POST"])
def payment_webhook():
    payload = request.get_json()

    if payload:
        processed_payments.append({
            "payment_id": payload.get("payment_id", "unknown"),
            "transaction_id": payload.get("transaction_id", "unknown"),
            "amount": payload.get("amount", 0),
            "status": payload.get("status", "unknown"),
            "processed_at": datetime.now().isoformat()
        })

    return jsonify({"received": True}), 200


@webhook_bp.route("/webhook/logs", methods=["GET"])
def logs():
    return jsonify({
        "total_processed": len(processed_payments),
        "payments": processed_payments
    })


@webhook_bp.route("/webhook/reset", methods=["POST"])
def reset():
    processed_payments.clear()
    return jsonify({"message": "reset"})