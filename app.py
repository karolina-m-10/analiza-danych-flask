from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    x1 = data.get('x1')
    x2 = data.get('x2')

    if x1 is None or x2 is None:
        return jsonify({'error': 'Missing parameters'}), 400

    decision = "High" if (x1 + x2) > 10 else "Low"

    return jsonify({'decision': decision})

if __name__ == '__main__':
    app.run(debug=True)
