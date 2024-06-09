from src.cook_raw import Cook
from src.LLM import LLM
from src.LLM_tune import LLM_tune
from src.vectorDB import VectorDB

from config import *
from utils import *

class Architect():
    def __init__(self):
        cook = Cook()
        self.author_sys_prompt = cook.retrieve_author_prompt()
        self.referee_sys_prompt = cook.retrieve_referee_prompt()
        
        self.prompter_finetune = LLM_tune(prompt_generator_model)
        self.prompt_generator = LLM(self.prompter_finetune.get_model())
        
        self.businese_plan_writer = LLM(businese_plan_writer_model)
        self.businese_plan_reviser = LLM(businese_plan_reviser_model)
        self.businese_plan_referee = LLM(businese_plan_referee_model)
        self.prompt_improver = LLM(prompt_improver_model)
        
        self.company_DB = VectorDB(company_DB_name)
        self.market_DB = VectorDB(market_DB_name)
        
        self.chosen_chunk = []
        
    def finetune_prompter(self):
        self.prompter_finetune.finetune()
        self.save_prompter()
        self.prompt_generator = LLM(self.prompter_finetune.get_model())
        
    def load_prompter(self):
        self.prompter_finetune.load_model(finetuned_model_path)
        
    def save_prompter(self):
        self.prompter_finetune.save_model(finetuned_model_path)
        
    def make_prompt(self, user_input):
        self.prompt_generator.start_new_chat(prompt_generator_system_prompt)
        prompt = self.prompt_generator.get_text_response(user_input)
        return prompt
    
    def retrieval(self, prompt):
        companyDB = VectorDB(company_DB_name)
        companyDB_search_result = companyDB.search_DB(prompt)
        marketDB = VectorDB(market_DB_name)
        marketDB_search_result = marketDB.search_DB(prompt)
        chosen_chunk = companyDB_search_result + marketDB_search_result
        self.chosen_chunk = chosen_chunk
        return chosen_chunk

    def write_businese_plan(self, prompt, chosen_chunk):
        self.businese_plan_writer.start_new_chat(self.author_sys_prompt)
        businese_plan = self.businese_plan_writer.get_text_response(
                                                    prompt, 
                                                    chosen_chunks_page=chosen_chunk)
        return businese_plan
    
    def revise_businese_plan(self, businese_plan, suggestion):
        self.businese_plan_reviser.start_new_chat(reviser_sys_prompt + suggestion)
        businese_plan = self.businese_plan_reviser.get_text_response(
                                                    businese_plan, 
                                                    chosen_chunks_page=self.chosen_chunk)
        return businese_plan
    
    def evaluate_businese_plan(self, businese_plan, chosen_chunk):
        self.businese_plan_referee.start_new_chat(self.referee_sys_prompt)
        evaluation = self.businese_plan_referee.get_text_response(
                                               businese_plan, 
                                               chosen_chunks_page=chosen_chunk)
        return evaluation
    
    def make_new_prompt(self, evaluation, prompt):
        self.prompt_improver.start_new_chat(prompt_improver_system_prompt)
        prompt = "**Prompt**" + prompt
        evaluation = "**Evaluation**" + evaluation
        input = prompt + "/n" + evaluation
        new_prompt = self.prompt_improver.get_text_response(input)
        return new_prompt
    
    def add_new_prompt_to_data(self, user_input, prompt):
        self.prompter_finetune.add_new_data(user_input, prompt)
        data_count = self.prompter_finetune.count_data()
        if data_count > data_count_upper_limit:
            self.prompter_finetune.delete_old_data(data_count - data_count_upper_limit)
            

            
        
    
    
        
        