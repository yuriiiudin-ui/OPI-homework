from flask import Flask, request, jsonify
from discount import DiscountCalculator

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint для перевірки працездатності застосунку."""
    return jsonify({"status": "ok"}), 200

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Endpoint для розрахунку знижки.
    Очікує JSON:
    {
        "customer_type": "standard" | "premium" | "vip",
        "amount": float,
        "qty": int (optional, default: 1)
    }
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Invalid JSON format"}), 400
        
    customer_type = data.get('customer_type')
    amount = data.get('amount')
    qty = data.get('qty', 1)
    
    if customer_type is None or amount is None:
        return jsonify({"error": "Missing required fields: 'customer_type' or 'amount'"}), 400
        
    try:
        calc = DiscountCalculator(customer_type)
        
        # Викликаємо bulk_discount, який сам розраховує кінцеву суму з урахуванням кількості
        final_price = calc.bulk_discount(float(amount), int(qty))
        
        return jsonify({
            "customer_type": customer_type,
            "original_amount": float(amount),
            "quantity": int(qty),
            "final_price": final_price
        }), 200
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
