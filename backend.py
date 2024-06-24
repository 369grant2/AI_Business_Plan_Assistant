from flask import Flask, request, jsonify
from src.inference import Inference

from config import *
from utils import *

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
                for _ in range(Regenerate_tolerance):
                    user_input = self.model.user_input_data_to_text(data)
                    business_plan = self.model.write_BP(user_input)
                    evaluation = self.model.evaluate_BP(business_plan, user_input)
                    total_score = extract_total_score(evaluation)
                    if total_score >= BP_score_threshold:
                        break
            else: # Revise BP wrtie
                for _ in range(Regenerate_tolerance):
                    business_plan, suggestion = self.model.user_suggestion_to_text(data)
                    business_plan = self.model.revise_BP(business_plan, suggestion)
                    evaluation = self.model.evaluate_BP(business_plan, business_plan)
                    total_score = extract_total_score(evaluation)
                    if total_score >= BP_score_threshold:
                        break
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
