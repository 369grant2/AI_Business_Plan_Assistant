### OpenAI config ###
OPENAI_API_KEY = 'sk-proj-rd6WrBE3V8eGfpRhvvMIT3BlbkFJ2kq46UUMe045E9ecn6xY' #VLDB api
# OPENAI_API_KEY = 'sk-proj-eCFiJNXyQxC53wcV5zSbT3BlbkFJ1bT9HjIQoBa1H7ZUNZtS' #P4DS api
# OPENAI_API_KEY = 'sk-proj-FmlT6SBnAQd2s3HTPGopT3BlbkFJTIr6IrdatEV93x6NsmY2' # Ghita
embedding_model = "text-embedding-3-small"
embedding_dim = 1536
### OpenAI config ###

### Pinecone config ###
PINECONE_API_KEY = '137ebb2d-af74-40dc-867d-8aaf19077243'
PINECONE_API_ENVIRONMENT = 'gcp-starter'
top_K = 20
### Pinecone config ###

### Raw data config ###
company_data = "./dat/raw/Company Data - Sheet1.csv"
finetuning_data = "./dat/raw/Finetuning Data.xlsx - Sheet1.csv"
market_data = "./dat/raw/Market Data - Tabellenblatt1.csv"
author_prompt = "./dat/raw/Prompter Template.docx.txt"
referee_prompt = "./dat/raw/Referee Template.txt"
### Raw data config ###

### DB config ###
company_DB_name = "company"
market_DB_name = "market"
### DB config ###

### LLM config ###
prompt_generator_model = "gpt-3.5-turbo-0125"
businese_plan_writer_model = "gpt-3.5-turbo-0125"
businese_plan_reviser_model = "gpt-3.5-turbo-0125"
businese_plan_referee_model = "gpt-3.5-turbo-0125"
prompt_improver_model = "gpt-3.5-turbo-0125" #"gpt-4o"
LLM_temperature = 0.9
LLM_max_tokens = 1000
### LLM config ###

### Prompt data config ###
training_data = "./dat/train.jsonl"
data_count_upper_limit = 18
### Prompt data config ###

### Finetuning config ###
finetuned_model_path = "./mdl/prompter.txt"
n_epochs = 1
batch_size = 32
learning_rate_multiplier = 0.5
### Finetuning config ###

### Training config ###
load_previous_model = False
iteration = 10
finetune_period = 5
### Training config ###

### Prompt_generator config ###
prompt_generator_system_prompt = \
    ""
### Plan sections config ###

### prompt improver config ###
prompt_improver_system_prompt = \
    "Rewrite new prompt based on given evaluation and previous prompt.\
     Previous prompt is started with **Prompt**, \
     and the evaluation is start with **Evaluation**."
### prompt improver config ###

### BP revisor config ###
reviser_sys_prompt = "Revise original plan with following suggestion: "
### BP revisor config ###