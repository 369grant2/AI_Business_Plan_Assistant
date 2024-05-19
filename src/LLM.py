import os
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain.schema import SystemMessage
from langchain.chains.question_answering import load_qa_chain
from config import *
from utils import *

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

class LLM():
    def __init__(self, LLM_model):
        self.chat = ChatOpenAI(model=LLM_model,
                                temperature=LLM_temperature,
                                )
        
    def start_new_chat(self, LLM_system_prompt):
        messages = [
            SystemMessage(
                content=LLM_system_prompt
            ),
        ]
        self.chat.invoke(messages)
        self.chain = load_qa_chain(self.chat)

    def get_text_response(self, LLM_human_prompt, chosen_chunks_page=None):
        self.response = self.chain.invoke({'input_documents': chosen_chunks_page,
                                           'question': LLM_human_prompt})
        return self.response['output_text']
