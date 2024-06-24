import re
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

            
def read_user_inputs(file_path):
    user_inputs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        json_lines = [json.loads(line) for line in file]
    for line in json_lines:
        user_inputs.append(line["messages"][1]["content"])
    return user_inputs

def read_prompts(file_path):
    prompts = []
    with open(file_path, 'r', encoding='utf-8') as file:
        json_lines = [json.loads(line) for line in file]
    for line in json_lines:
        prompts.append(line["messages"][2]["content"])
    return prompts

expected_structure = {
    "messages": [
        {"role": "system", "content": ""},
        {"role": "user", "content": ""},
        {"role": "assistant", "content": ""}
    ]
}

def validate_structure(data_item, expected_structure):
    if isinstance(data_item, dict) and isinstance(expected_structure, dict):
        return set(data_item.keys()) == set(expected_structure.keys())
    if isinstance(data_item, list) and isinstance(expected_structure, list):
        return all(validate_structure(i, expected_structure[0]) for i in data_item)
    return False

def extract_total_score(evlaution):
    match = re.search(r'Total_score=\s*(\d+)', evlaution)
    if match:
        total_score = int(match.group(1))
    else:
        total_score = 0
    return total_score
