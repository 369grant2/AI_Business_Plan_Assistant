### OpenAI config ###
OPENAI_API_KEY = "" #P4DS api
embedding_model = "text-embedding-3-small"
embedding_dim = 1536
### OpenAI config ###

### Pinecone config ###
PINECONE_API_KEY = '0af25f95-58b5-44ba-a623-331460ab68e3'
PINECONE_API_ENVIRONMENT = 'gcp-starter'
top_K = 20
### Pinecone config ###

### Raw data config ###
company_data = "./dat/raw/Company Data - Sheet1.csv"
finetuning_data = "./dat/raw/Finetuning Data.xlsx - Sheet1.csv"
market_data = "./dat/raw/Market Data - Tabellenblatt1.csv"
prompter_prompt = "./dat/raw/Prompter Template.docx.txt"
author_prompt = "./dat/raw/Author Template.docx.txt"
referee_prompt = "./dat/raw/Referee Template.txt"
### Raw data config ###

### DB config ###
company_DB_name = "company"
market_DB_name = "market"
### DB config ###

### LLM config ###
prompt_generator_model = "gpt-3.5-turbo-0125"
businese_plan_writer_model = "gpt-4o"
businese_plan_reviser_model = "gpt-4o"
businese_plan_referee_model = "gpt-4o"
prompt_improver_model = "gpt-4o"
LLM_temperature = 0.9
LLM_max_tokens = 2000
### LLM config ###

### Prompt data config ###
training_data = "./dat/train.jsonl"
data_count_upper_limit = 64
### Prompt data config ###

### Finetuning config ###
finetuned_model_path = "./mdl/prompter.txt"
n_epochs = 10
batch_size = 32
learning_rate_multiplier = 0.9
### Finetuning config ###

### Training config ###
load_previous_model = False
iteration = 300
finetune_period = 10
### Training config ###

### prompt improver config ###
prompt_improver_system_prompt = \
    "Rewrite new prompt based on given evaluation and previous prompt.\
     Previous prompt is started with **Prompt**, \
     and the evaluation is start with **Evaluation**."
### prompt improver config ###

### BP revisor config ###
reviser_sys_prompt = "Revise original plan with following suggestion: "
### BP revisor config ###

### Backend config ###
BP_score_threshold = 10 # BP need to achieve this score from referee
Regenerate_tolerance = 3 # If author can not achieve the threshold many times, output anyway
### Backend config ###