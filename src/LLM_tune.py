import os
import time
import json
from openai import OpenAI
from config import *
from utils import *

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

class LLM_tune():
    def __init__(self, model):
        self.client = OpenAI()
        self.model = model
        
    def finetune(self):
        self.training_file = self.client.files.create(file=open(training_data, "rb"), purpose="fine-tune")
        self.response = self.client.fine_tuning.jobs.create(
            model=self.model,
            training_file=self.training_file.id,
            hyperparameters = {"n_epochs" : n_epochs,
                               "batch_size" : batch_size,
                               "learning_rate_multiplier" : learning_rate_multiplier
                               }
        )
        self.id = self.response.id
        print("Finetuning job id: ", self.id)
        status = self.get_status()
        while status not in ["succeeded", "failed"]:
            status = self.get_status()
            print(f"Fine-tuning status: {status}")
            time.sleep(10)
            
        self.model = self.get_model()
        if self.get_status() == "succeeded":
            print("Fine-tuning completed successfully!")
            print("Model name: ", self.model)
        else:
            print("Fine-tuning failed.")
            
    def get_status(self):
        try:
            return self.response.status
        except AttributeError:
            return "Status unavailable"

    def get_model(self):
        status = self.get_status()
        if status == 'succeeded':
            print("Using finetuned model")
            return self.response.fine_tuned_model
        else:
            print("Using default model")
            return self.model
        
    def load_model(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            self.model = file.read()
            print("Load model: ", self.model)
            return self.model

    def save_model(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.model)
            print("Model saved to ", filename)

    def add_new_data(self, prompt, completion):
        new_data = {
                "messages": [
                    {"role": "system", "content": ""},
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": completion}
                ]
            }
        with open(training_data, 'a', encoding='utf-8') as file:
            file.write(json.dumps(new_data) + '\n')

    def count_data(self):
        try:
            line_count = 0
            with open(training_data, 'r', encoding='utf-8') as file:
                for line in file:
                    line_count += 1
        except Exception as e:
            print(f"Unable to read: {e}")
            return
        return line_count

    def delete_old_data(self, cnt):
        with open(training_data, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        remaining_lines = lines[cnt:]

        with open(training_data, 'w', encoding='utf-8') as file:
            file.writelines(remaining_lines)