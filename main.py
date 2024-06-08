from src.cook_raw import Cook
from src.train import Train
from src.LLM_tune import LLM_tune

from config import *
from utils import *

def main():
    # cook = Cook()
    # cook.retrieve_finetuning_pairs()
    LLM_Tune = LLM_tune(prompt_generator_model)
    LLM_Tune.finetune()
    # train = Train()
    # train.finetune_prompter()
        
if __name__ == "__main__":
    main()