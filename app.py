from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/decode', methods=['POST'])
def decode():
    data = request.get_json()
    code = data.get('code')

    # Exemple fixe pour tester
    response = [
        {"product_name": "AQL-C+", "quantity": 1},
        {"product_name": "OPT-AQL-IN", "quantity": 2}
    ]

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
