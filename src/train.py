from src.architect import Architect

from config import *
from utils import *

class Train():
    def __init__(self):
        self.architect = Architect()
        if load_previous_model:
            self.architect.load_prompter()
        
    def __iter(self, user_input, finetune = False):
        if finetune:
            self.architect.finetune_prompter()
        prompt = self.architect.make_prompt(user_input)
        chosen_chunk = self.architect.retrieval(prompt)
        businese_plan = self.architect.write_businese_plan(prompt, chosen_chunk)
        evaluation = self.architect.evaluate_businese_plan(businese_plan, chosen_chunk)
        new_prompt = self.architect.make_new_prompt(evaluation, prompt)
        self.architect.add_new_prompt_to_data(user_input, new_prompt)
        
    def __iter_temp(self, user_input, prompt, finetune = False):
        if finetune:
            self.architect.finetune_prompter()
        chosen_chunk = self.architect.retrieval(prompt)
        businese_plan = self.architect.write_businese_plan(prompt, chosen_chunk)
        # print("\n\n\n\n\n\n")
        # print("businese_plan")
        # print(businese_plan)
        evaluation = self.architect.evaluate_businese_plan(businese_plan, chosen_chunk)
        # print("\n\n\n\n\n\n")
        # print("evaluation")
        # print(evaluation)
        new_prompt = self.architect.make_new_prompt(evaluation, prompt)
        # print("\n\n\n\n\n\n")
        # print("new_prompt")
        # print(new_prompt)
        self.architect.add_new_prompt_to_data(user_input, new_prompt)
        
    def run(self):
        user_inputs = read_user_inputs(training_data)
        prompts = read_prompts(training_data)
        for i in range(iteration):
            print("Training iteration ", i)
            if (i % finetune_period == 0):
                finetune = True
                print("Performing finetuning", finetune)
            else:
                finetune = False
            user_input = user_inputs[i % len(user_inputs)]
            prompt = prompts[i % len(user_inputs)]
            # self.__iter_temp(user_input, prompt, finetune)
            self.__iter(user_input, finetune)
        print("Training complete")

        
        