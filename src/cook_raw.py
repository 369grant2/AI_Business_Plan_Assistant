from config import *
from utils import *

class Cook():
    def __init__(self):
        self.company_data = company_data
        self.finetuning_data = finetuning_data
        self.market_data = market_data
        self.prompter_prompt = prompter_prompt
        self.author_prompt = author_prompt
        self.referee_prompt = referee_prompt
        
    def retrieve_prompter_prompt(self):
        return read_txt_file(self.prompter_prompt)
        
    def retrieve_author_prompt(self):
        return read_txt_file(self.author_prompt)
    
    def retrieve_referee_prompt(self):
        return read_txt_file(self.referee_prompt)
    
    def retrieve_finetuning_pairs(self):
        return read_csv_pairs(self.finetuning_data, training_data)
    
    def retrieve_company_data(self):
        return read_csv_file(self.company_data)
    
    def retrieve_market_data(self):
        return read_csv_file(self.market_data)