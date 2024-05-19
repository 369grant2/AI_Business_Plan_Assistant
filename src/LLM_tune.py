import os
import time
import json
import openai
from config import *
from utils import *

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

class LLM_tune():
    def __init__(self):
        self.training_file = openai.File.create(file=open(training_data, "rb"), purpose="fine-tune")
        """
        {"prompt": "Translate English to French: cheese", "completion": "fromage"}
        {"prompt": "Translate English to French: apple", "completion": "pomme"}
        {"prompt": "What is the capital of France?", "completion": "The capital of France is Paris."}
        """
        
    def add_new_data(self, prompt, completion):
        new_data = {"prompt": prompt, "completion": completion}
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
            
    def finetune(self, model):
        self.fine_tune = openai.FineTune.create(
            model=model,
            training_file=self.training_file.id,
            n_epochs=n_epochs,
            batch_size=batch_size,
            learning_rate_multiplier=learning_rate_multiplier
        )

        status = self.fine_tune['status']
        while status not in ["succeeded", "failed"]:
            self.fine_tune = openai.FineTune.retrieve(self.fine_tune['id'])
            status = self.fine_tune['status']
            print(f"Fine-tuning status: {status}")
            time.sleep(10)

        if status == "succeeded":
            print("Fine-tuning completed successfully!")
        else:
            print("Fine-tuning failed.")
            
    def get_model(self):
        if self.fine_tune['status'] == 'succeeded':
            return self.fine_tune['fine_tuned_model']
        else:
            raise ModuleNotFoundError
