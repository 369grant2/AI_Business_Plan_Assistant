from src.architect import Architect

from config import *
from utils import *

class Inference():
    def __init__(self):
        self.architect = Architect()
        self.architect.load_prompter()
        
    def user_input_data_to_text(self, data):
        user_input = f"""
            Business Idea: {data['business_overview']}
            Problem Statement/Pain Point: {data['mission_vision_statements']}
            Goals and Scope: {data['mission_vision_statements']}
            Management Team/Expertise: {', '.join([member['expertise'] for member in data['team_members']])}
            Business Structure: {data['business_structure']} model targeting municipalities, waste management companies, and large corporations
            Unique Value Proposition: {data['unique_value_proposition']}
            Industry Description: {data['industry_description']}
            Demographics of Target Market: {data['target_market']}
            Geographical Location of Target Market: Initially focused on {data['geographical_location']}
            Product/Service Description: {data['product_service_description']}
            Key Features: {data['key_features']}
            Key Benefits: {data['key_benefits']}
            """
        return user_input
    
    def user_suggestion_to_text(self, data):
        businese_plan = data["business_plan"]
        suggestion = data["revise_request"]
        return businese_plan, suggestion
        
    def write_BP(self, user_input):
        prompt = self.architect.make_prompt(user_input)
        chosen_chunk = self.architect.retrieval(prompt)
        businese_plan = self.architect.write_businese_plan(prompt, chosen_chunk)
        return businese_plan
    
    def evaluate_BP(self, businese_plan, user_input):
        prompt = self.architect.make_prompt(user_input)
        chosen_chunk = self.architect.retrieval(prompt)
        evaluation = self.architect.evaluate_businese_plan(businese_plan, chosen_chunk)
        return evaluation
    
    def revise_BP(self, businese_plan, suggestion):
        businese_plan = self.architect.revise_businese_plan(businese_plan, suggestion)
        return businese_plan
