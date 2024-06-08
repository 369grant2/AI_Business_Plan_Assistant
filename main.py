import subprocess
import time

from src.cook_raw import Cook
from src.train import Train

from config import *
from utils import *

def main():
    # cook = Cook()
    # cook.retrieve_finetuning_pairs()
    # train = Train()
    # train.run()
    
    process_UI = subprocess.Popen(["streamlit", "run", "app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process_backend = subprocess.Popen(["python3", "backend.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    while (process_UI.poll() is None) and (process_backend.poll() is None):
        print("Program operating")
        time.sleep(1)
    
        
if __name__ == "__main__":
    main()