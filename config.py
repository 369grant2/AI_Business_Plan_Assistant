### OpenAI config ###
OPENAI_API_KEY = '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'
embedding_model = "text-embedding-3-small"
### OpenAI config ###

### Pinecone config ###
PINECONE_API_KEY = '0af25f95-58b5-44ba-a623-331460ab68e3'
PINECONE_API_ENVIRONMENT = 'gcp-starter'
PINECONE_INDEX_NAME = 'document-answer-langchain-pinecone-openai'
### Pinecone config ###

### LLM config ###
prompt_generator_model = "gpt-3.5-turbo-0125"
businese_plan_writer_model = "gpt-4-1106-preview"
businese_plan_referee_model = "gpt-4-1106-preview"
prompt_improver_model = "gpt-4-1106-preview"
LLM_temperature = 0.9
### LLM config ###

### Prompt data config ###
training_data = "./dat/train.jsonl"
data_count_upper_limit = 100
### Prompt data config ###

### Training config ###
n_epochs = 10
batch_size = 32
learning_rate_multiplier = 0.5
### Training config ###

### Prompt_generator config ###
prompt_generator_system_prompt = \
    "Generate a prompt based on given keyword and section name."
sections = [
    "section 1 name",
    "section 2 name",
    "section 3 name",
]
### Plan sections config ###

### businese_plan_writer config ###
businese_plan_writer_system_prompt = \
    "Generate businese report based on given prompt and reference."
### businese_plan_writer config ###

### businese_plan_writer config ###
businese_plan_writer_system_prompt = \
    "Generate criticize based on given businese report."
### businese_plan_writer config ###

### businese_plan_writer config ###
prompt_improver_system_prompt = \
    "Generate new prompt based on given criticize and previous prompt."
### businese_plan_writer config ###