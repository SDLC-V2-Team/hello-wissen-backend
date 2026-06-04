from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/greeting', methods=['GET'])
def hello_wissen():
    """Return the greeting 'Hello Wissen'."""
    return jsonify({'message': 'Hello Wissen'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
