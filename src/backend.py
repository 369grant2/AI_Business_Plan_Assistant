from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.json
    print("Received data:", data)
    return jsonify({"status": "success", "message": "Data received successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
