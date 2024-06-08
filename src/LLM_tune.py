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
        self.training_file = self.client.files.create(file=open(training_data, "rb"), purpose="fine-tune")
        """
        {"prompt": "Translate English to French: cheese", "completion": "fromage"}
        {"prompt": "Translate English to French: apple", "completion": "pomme"}
        {"prompt": "What is the capital of France?", "completion": "The capital of France is Paris."}
        """
        
    def load_model(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            self.model = file.read()
            print("Load model: ", self.model)
            return self.model

    def save_model(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.model)
            print("Model saved to ", filename)
        
    def finetune(self):
        self.fine_tune = self.client.fine_tuning.jobs.create(
            model=self.model,
            training_file=self.training_file.id,
            hyperparameters = {"n_epochs" : n_epochs,
                               "batch_size" : batch_size,
                               "learning_rate_multiplier" : learning_rate_multiplier
                               }
        )
        self.id = self.fine_tune.id
        print("Finetuning job id: ", self.id)
        status = self.get_status()
        while status not in ["succeeded", "failed"]:
            status = self.get_status()
            print(f"Fine-tuning status: {status}")
            time.sleep(10)
            
        self.model = self.get_model()
        if status == "succeeded":
            print("Fine-tuning completed successfully!")
            print("Model name: ", self.model)
        else:
            print("Fine-tuning failed.")
            
    def get_status(self):
        return self.fine_tune.status

    def get_model(self):
        status = self.get_status()
        if status == 'succeeded':
            print("Using finetuned model")
            return self.fine_tune.fine_tuned_model
        else:
            print("Using default model")
            return self.model

    def add_new_data(self, prompt, completion):
        new_data = {
                "messages": [
                    {"role": "system", "content": ""},
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": completion}
                ]
            }
        json.dump(new_data, self.training_file)
        self.training_file.write('\n')

    def count_data(self):
        try:
            self.training_file.seek(0)
            data = self.training_file.readlines()
        except Exception as e:
            print(f"Unable to read：{e}")
            return
        return len(data)

    def delete_old_data(self, cnt):
        try:
            self.training_file.seek(0)
            data = self.training_file.readlines()
        except Exception as e:
            print(f"Unable to read：{e}")
            return

        if len(data) <= cnt:
            print("Insufficient data count to delete")
            return

        updated_data = data[cnt:]

        try:
            self.training_file.seek(0)
            self.training_file.truncate() 
            self.training_file.writelines(updated_data) 
        except Exception as e:
            print(f"Unable to perform file update：{e}")