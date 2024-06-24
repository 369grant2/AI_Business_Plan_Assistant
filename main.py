import subprocess
import time

from src.vectorDB import VectorDB
from src.cook_raw import Cook
from src.train import Train

from config import *
from utils import *

def main():
    # cook = Cook()
    # cook.retrieve_finetuning_pairs()
    # company_data = cook.retrieve_company_data()
    # market_data = cook.retrieve_market_data()
    
    # company_DB = VectorDB(company_DB_name)
    # company_DB.reset_DB()
    # company_DB.create_DB(company_data)
    # market_DB = VectorDB(market_DB_name)
    # market_DB.reset_DB()
    # market_DB.create_DB(market_data)
    
    # train = Train()
    # train.run()

    process_UI = subprocess.Popen(["streamlit", "run", "app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process_backend = subprocess.Popen(["python3", "backend.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    while (process_UI.poll() is None) and (process_backend.poll() is None):
        print("Program operating")
        time.sleep(10)
    
        
if __name__ == "__main__":
    main()