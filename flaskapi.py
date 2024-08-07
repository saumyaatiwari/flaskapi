from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def get_hello():
    return jsonify(message='Hello, World!')

if __name__ == '__main__':
    app.run()
