from flask import Flask
from routes.checkout import checkout_bp
from routes.orders import orders_bp
from routes.webhook import webhook_bp

app = Flask(__name__)

app.register_blueprint(checkout_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(webhook_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)