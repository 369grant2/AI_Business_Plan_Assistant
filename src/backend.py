from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.json
    processed_data = {
        "message": "Data processed successfully",
        "received_data": "Monk DB"
    }
    return jsonify(processed_data), 200

if __name__ == '__main__':
    app.run(debug=True)
