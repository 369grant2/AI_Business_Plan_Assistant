from src.cook_raw import Cook
from src.LLM import LLM
from src.LLM_tune import LLM_tune
from src.vectorDB import VectorDB

from config import *
from utils import *

class Architect():
    def __init__(self):
        cook = Cook()
        self.author_prompt = cook.retrieve_author_prompt()
        self.referee_prompt = cook.retrieve_referee_prompt()
        
        self.prompter_finetune = LLM_tune(prompt_generator_model)
        
        self.businese_plan_writer = LLM(businese_plan_writer_model)
        self.businese_plan_referee = LLM(businese_plan_referee_model)
        self.prompt_improver = LLM(prompt_improver_model)
        
        self.company_DB = VectorDB(company_DB_name)
        self.market_DB = VectorDB(market_DB_name)
        
    def finetune_prompter(self):
        self.prompter_finetune.finetune()
        self.save_prompter()
        self.prompt_generator = LLM(self.prompter_finetune.get_model())
        
    def load_prompter(self):
        self.prompter_finetune.load_model(finetuned_model_path)
        
    def save_prompter(self):
        self.prompter_finetune.save_model(finetuned_model_path)
        
    def make_prompts(self, keywords):
        self.prompt_generator.start_new_chat(prompt_generator_system_prompt)
        prompt = self.prompt_generator.get_text_response(keywords)
        return prompt
    
    def retrieval(self, prompt):
        companyDB = VectorDB(company_DB_name)
        companyDB_search_result = companyDB.search_DB()
        marketDB = VectorDB(market_DB_name)
        marketDB_search_result = marketDB.search_DB()
        self.chosen_chunk = companyDB_search_result + marketDB_search_result

    def write_businese_plan(self, prompt):
        self.businese_plan_writer.start_new_chat(self.author_prompt)
        plan = self.businese_plan_writer.get_text_response(
                                        prompt, 
                                        chosen_chunks_page=self.chosen_chunk)
        return plan
    
    def crticize_businese_plan(self, businese_plan):
        self.businese_plan_referee.start_new_chat(self.referee_prompt)
        criticize = self.businese_plan_referee.get_text_response(
                                               businese_plan, 
                                               chosen_chunks_page=self.chosen_chunk)
        return criticize
    
    def make_new_prompt(self, criticize, prompt):
        self.prompt_improver.start_new_chat(prompt_improver_system_prompt)
        prompt = "**Prompt**" + prompt
        criticize = "**Evaluation**" + criticize
        input = prompt + "/n" + criticize
        new_prompt = self.prompt_improver.get_text_response(input)
        return new_prompt
    
    def add_new_prompt_to_data(self, keywords, prompt):
        self.prompter_finetune.add_new_data(keywords, prompt)
        data_count = self.prompter_finetune.count_data()
        if data_count > data_count_upper_limit:
            self.prompter_finetune.delete_old_data(self, data_count - data_count_upper_limit)
            

            
        
    
    
        
        