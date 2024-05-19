from src.LLM import LLM
from src.LLM_tune import LLM_tune
from VectorDB import VectorDB

from config import *
from utils import *

class Train():
    def __init__(self):
        self.prompt_generator = LLM(prompt_generator_model)
        self.businese_plan_writer = LLM(businese_plan_writer_model)
        self.businese_plan_referee = LLM(businese_plan_referee_model)
        self.prompt_improver = LLM(prompt_improver_model)
        self.finetune = LLM_tune()
        self.VectorDB = VectorDB()
        
    def make_section_prompts(self, keywords):
        self.prompt_generator.start_new_chat(prompt_generator_system_prompt)
        prompt = self.prompt_generator.get_text_response(input)
        return prompt
    
    def write_businese_plan(self, prompt):
        self.businese_plan_writer.start_new_chat(businese_plan_writer_system_prompt)
        plan = []
        for section in sections:
            section_prompt  = prompt + section
            reference = self.VectorDB.search_DB(section_prompt)
            plan_of_section = self.businese_plan_writer.\
                              get_text_response(section_prompt, reference)
            plan.append(plan_of_section)
        return plan.join("\n")
    
    def crticize_businese_plan(self, businese_plan):
        self.businese_plan_referee.start_new_chat(businese_plan_writer_system_prompt)
        criticize = self.businese_plan_referee.get_text_response(businese_plan)
        return criticize
    
    def make_new_prompt(self, criticize, prompt):
        self.prompt_improver.start_new_chat(prompt_improver_system_prompt)
        prompt = "**prompt**" + prompt
        criticize = "**criticize**" + criticize
        input = prompt + "/n" + criticize
        new_prompt = self.prompt_improver.get_text_response(input)
        return new_prompt
    
    def add_new_prompt_to_data(self, keywords, prompt):
        self.finetune.add_new_data(keywords, prompt)
        data_count = self.finetune.count_data()
        if data_count > data_count_upper_limit:
            self.finetune.delete_old_data(self, data_count - data_count_upper_limit)
            
    def finetune_prompter(self):
        self.finetune.finetune(self.prompt_generator)
        self.prompt_generator = self.finetune.get_model()
            
        
    
    
        
        