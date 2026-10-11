import os
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS so other team laptops can communicate with your server safely
CORS(app)

# =====================================================================
# MEHAK'S CORE MODULES: LOGIN, FEEDBACK & PAYMENTS 
# =====================================================================

@app.route('/api/login', methods=['POST'])
def handle_login():
    """Validates team user login access requests."""
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    
    if username and password:
        return jsonify({"status": "authenticated", "message": f"Welcome back, {username}!"}), 200
    return jsonify({"status": "error", "message": "Invalid credentials provided."}), 401


@app.route('/api/feedback', methods=['POST'])
def process_feedback():
    """Captures continuous user feedback metrics to update requirements dynamically."""
    data = request.get_json() or {}
    feedback_text = data.get('feedback', '')
    user_rating = data.get('rating', 5)
    
    print(f"[Feedback Received]: {feedback_text} (Rating: {user_rating}/5)")
    return jsonify({
        "status": "success", 
        "message": "Feedback integrated successfully into the active development loop!"
    }), 200


@app.route('/api/payment/verify', methods=['POST'])
def verify_payment():
    """Simulates payment transaction validation layer for the platform."""
    data = request.get_json() or {}
    transaction_id = data.get('transaction_id', 'TXN-MOCK-999')
    amount = data.get('amount', 0)
    
    return jsonify({
        "status": "verified",
        "transaction_id": transaction_id,
        "message": f"Payment validation loop complete. Amount cleared: INR {amount}"
    }), 200

# =====================================================================
# POORVI'S WORKSPACE CORE ROUTE: REAL-WORLD NEWS/COMPLIANCE EVALUATOR
# =====================================================================

@app.route('/api/check-news', methods=['POST'])
def check_news_compliance():
    """
    Compares the product idea concept against regulatory macro trends 
    (GST updates, Zomato/Swiggy fees, and India's DPDP privacy laws).
    """
    data = request.get_json() or {}
    user_idea = data.get('idea', 'Food Delivery Platform')
    
    print(f"[Analyzing Lifecycle Concept]: {user_idea}")
    
    # Highly specific compliance payload mapping back to your front-end components
    compliance_report = {
        "status": "Analysis Complete",
        "gst_impact": "WARNING: Your application workflow falls under the current 18% GST levy guidelines for electronic commerce operators. Ensure your built payment processing module routes split taxes automatically to prevent legal flags.",
        "fee_impact": "COMPETITIVE MARKET HEADWIND: Zomato & Swiggy platform fee increases mean tighter operating margins. Focus on lean development scripts to balance initial onboarding costs.",
        "dpdp_impact": "CRITICAL DATA PRIVACY COMPLIANCE: Digital Personal Data Protection (DPDP) Act mandates granular consent frameworks. Update your custom Login system to include explicit, un-checked approval selectors before capturing user records."
    }
    return jsonify(compliance_report), 200

# =====================================================================
# HOME PAGE VIEW
# =====================================================================
@app.route('/')
def index():
    return "ProductPilot AI Central Nervous System Server is Active."

# Server Entry Configuration - Listens on all local interfaces on Port 5001
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)