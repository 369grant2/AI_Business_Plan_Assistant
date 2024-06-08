
import csv
import json
from langchain_community.document_loaders.csv_loader import CSVLoader

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def read_csv_file(file_path):
    loader = CSVLoader(file_path)
    data = loader.load()
    return data

def read_csv_pairs(csv_path, jsonl_path):
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        jsonl_lines = []
        
        for row in reader:
            jsonl_obj = {
                "messages": [
                    {"role": "system", "content": ""},
                    {"role": "user", "content": row[reader.fieldnames[1]]},
                    {"role": "assistant", "content": row[reader.fieldnames[2]]}
                ]
            }
            jsonl_lines.append(json.dumps(jsonl_obj))
        
        jsonl_content = '\n'.join(jsonl_lines)
        
        with open(jsonl_path, 'w', encoding='utf-8') as jsonlfile:
            jsonlfile.write(jsonl_content)
