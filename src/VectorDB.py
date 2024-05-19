from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

from config import *
from utils import *


class VectorDB():
    def __init__(self):
        pinecone.init(
            api_key=PINECONE_API_KEY,
            environment=PINECONE_API_ENVIRONMENT
        )
        embeddings = OpenAIEmbeddings(client=embedding_model)
        self.docsearch = pinecone.from_existing_index(
                                    index_name=PINECONE_INDEX_NAME,
                                    embedding=embeddings)

    def search_DB(self, query):
        search_result = self.docsearch.similarity_search(query)
        return search_result
