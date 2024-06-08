from flask import Flask, request, jsonify
from src.inference import Inference

class MyFlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()
        self.model = Inference()

    def setup_routes(self):
        @self.app.route('/receive-data', methods=['POST'])
        def receive_data():
            data = request.json
            user_input = self.model.user_input_data_to_text(data)
            business_plan = self.model.write_BP(user_input)
            processed_data = {
                "message": "Data processed successfully",
                "received_data": business_plan
            }
            return jsonify(processed_data), 200

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    app_instance = MyFlaskApp()
    app_instance.run()
