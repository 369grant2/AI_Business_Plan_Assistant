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
            if "business_plan" not in data: # Regular BP wrtie
                user_input = self.model.user_input_data_to_text(data)
                business_plan = self.model.write_BP(user_input)
                evaluation = self.model.evaluate_BP(business_plan, user_input)
            else: # Revise BP wrtie
                business_plan, suggestion = self.model.user_suggestion_to_text(data)
                business_plan = self.model.revise_BP(business_plan, suggestion)
                evaluation = self.model.evaluate_BP(business_plan, business_plan)
            processed_data = {
                "message": "Data processed successfully",
                "business_plan": business_plan,
                "evaluation": evaluation,
            }
            return jsonify(processed_data), 200

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    app_instance = MyFlaskApp()
    app_instance.run()
